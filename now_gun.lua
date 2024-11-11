local address = "output.lua"    -- 地址, output.lua


local function is_authorized()  -- 是否授权, 用于检查是否加载了weapon.lua
    local success, chunk = pcall(dofile, addr)  -- 加载weapon.lua

    if not success then -- 如果加载失败
        OutputLogMessage("Error loading weapon.lua: %s\n", chunk)   -- 输出错误信息
        return false    -- 返回false
    end -- 如果加载成功, 则返回true
        return true
end -- 函数结束


function read_weapon_from_file()    -- 从文件中读取武器
    if not is_authorized() then -- 如果没有授权
        return nil  -- 返回nil
    end
    weapon = nil
    scopes = nil
    muzzles = nil
    stocks= nil
    poses = nil
    shoot = nil
    car = nil

    dofile(addr)    -- 加载weapon.lua

    if weapon_name then -- 如果有武器名

        last_weapon = weapon
        last_muzzles = muzzle
        last_grips = grip
        last_scopes = scope
        last_stocks = stock
        last_poses = pose
        last_shoot = shoot
        last_car = car

        local output = string.format("%s+%s+%s+%s+%s+%s+%s+%s+%s",weapon, muzzle, grip, scope, stock, pose
        , scope, shoot, car)  -- 输出信息, 格式化字符串, 传入武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 射击, 载具
        OutputLogMessage("%s\n", output)        -- 输出信息, 传入信息
        return weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, shoot, car   -- 返回武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 射击, 载具
    else
        OutputLogMessage("未找到武器信息, 使用上一次的武器信息\n")

        return last_weapon_name, last_muzzles, last_grips, last_scopes, last_stocks, last_poses, last_scope_zoom, last_shoot, last_car  -- 返回上一次的武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 射击, 载具
    end
end


local decimal_cache = 0 -- 用于缓存小数部分，以便在下一次调用时使用

-- 以下是向上取整并缓存小数部分的函数
function ceil_and_cache(value)
    local integer_part = math.floor(value)  -- 取整部分
    decimal_cache = decimal_cache + value - integer_part    -- 小数部分
    if decimal_cache >= 1 then  -- 如果小数部分大于等于1
        integer_part = integer_part + 1 -- 整数部分加1
        decimal_cache = decimal_cache - 1   -- 小数部分减1
    end
    return integer_part -- 返回向上取整后的值
end


-- 以下是压枪倍率计算的函数, 传入武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 载具
function calculate_recoil_multiplier(weapon, muzzle, grip, scope, stock, pose, car)
    local multiplier = global_recoil_multiplier     -- 全局压枪倍率, 默认为1
    local weaponData = attachment_multipliers[weapon_name]  -- 武器数据, 配件倍率

    multiplier = multiplier * (base_coefficients[weapon_name] or 1)     -- 基础倍率

    if weaponData then   -- 如果有武器数据
        multiplier = multiplier * (weaponData.poses[poses] or 1)    -- 姿势倍率
        multiplier = multiplier * (weaponData.muzzles[muzzles] or 1)    -- 枪口倍率
        multiplier = multiplier * (weaponData.grips[grips] or 1)    -- 握把倍率
        multiplier = multiplier * (weaponData.scopes[scopes] or 1)  -- 瞄准镜倍率
        multiplier = multiplier * (weaponData.stocks[stocks] or 1)  -- 枪托倍率
        multiplier = multiplier * (weaponData.car[car] or 1)    -- 载具倍率
        multiplier = multiplier * scope_zoom    -- 瞄准倍率
    end -- 如果没有武器数据，则不做任何处理

    multiplier = multiplier * (global_scope_multipliers[scopes] or 1)   -- 全局瞄准倍率

    if IsModifierPressed("lshift") then -- 如果按下了左shift键
        multiplier = multiplier * global_breath_multiplier  -- 呼吸倍率
    end -- 如果没有按下左shift键，则不做任何处理

    return multiplier   -- 返回计算后的倍率
end -- 函数结束



local burstModeEnabled = false  -- 是否启用burst模式
local debugModeEnabled = false  -- 是否启用调试模式


local weaponBurstModes = {} -- 武器burst模式


local ClickStartTime = 0    -- 开始射击时间

-- 以下是压枪函数
local function is_authorized()  -- 是否授权, 用于检查是否加载了weapon.lua
    local success, chunk = pcall(dofile, addr)  -- 加载weapon.lua

    if not success then -- 如果加载失败
        OutputLogMessage("Error loading weapon.lua: %s\n", chunk)   -- 输出错误信息
        return false    -- 返回false
    end -- 如果加载成功, 则返回true
        return type(muzzle) == "string" and muzzle == "None"    -- 返回muzzle是否是字符串且等于"None"
end -- 函数结束

-- 以下是压枪函数
for weapon_name, patterns in pairs(recoil_patterns) do  -- 遍历压枪数据, weapon_name是武器名, patterns是压枪数据
    for pattern_type, pattern in pairs(patterns) do     -- 遍历压枪数据, pattern_type是压枪类型, pattern是压枪数据
        for i, data in ipairs(pattern) do       -- 遍历压枪数据, i是索引, data是数据
            if i % 2 == 0 then  -- 如果索引是偶数
                pattern[i][2] = (pattern[i][2] + 1) / 2     -- 压枪数据, 偶数索引的数据
            end
        end
    end
end

-- 以下是压枪函数, 用于应用压枪
function apply_recoil(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom)   -- 应用压枪
    if not is_authorized() then -- 如果没有授权
        return  -- 不做任何处理
    end -- 如果授权了, 则继续执行
    local pattern_type = IsModifierPressed("rshift") and "burst" or "default"   -- 压枪类型, 如果按下了右shift键, 则是burst模式, 否则是默认模式
    local pattern = recoil_patterns[weapon_name] and recoil_patterns[weapon_name][pattern_type] or
            recoil_patterns[weapon_name]  -- 压枪数据, 如果有武器数据, 则使用武器数据, 否则使用默认数据
    local interval = weapon_intervals[weapon_name]      -- 压枪间隔, 武器间隔, 如果没有则使用默认间隔

    if not pattern or not interval then     -- 如果没有压枪数据或者没有间隔, 则不做任何处理
        OutputLogMessage("未找到武器的压枪参数: %s\n", weapon_name)       -- 输出错误信息
        return
    end

    local multiplier = calculate_recoil_multiplier(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom,
            car)     -- 压枪倍率, 计算压枪倍率, 传入武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 载具
    local bullet_count = 0  -- 子弹数, 初始化为0

    if weapon_name == "MK47" or weapon_name == "M16"  or weapon_name == "None" or weapon_name == "MINI" or
            weapon_name == "SKS" or weapon_name == "MK12" or weapon_name == "SLR" or weapon_name == "QBU" then       -- 如果是MK47或者M16 或者None  或者MINI 或者SKS 或者MK12 或者SLR 或者QBU,

        while IsMouseButtonPressed(1) do        -- 如果鼠标左键按下
            if shoot == "None" then
                break
            end
            local ClickCurrentTime = GetRunningTime()    -- 当前时间
            bullet_count = math.ceil((ClickCurrentTime - ClickStartTime) / interval)    -- 子弹数, 向上取整, 传入当前时间和开始时间, 除以间隔

            for _, recoil_data in ipairs(pattern) do       -- 遍历压枪数据, recoil_data是压枪数据
                if recoil_data[1] == bullet_count then     -- 如果压枪数据的子弹数等于子弹数
                    multiplier = calculate_recoil_multiplier(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom,
                            car)     -- 压枪倍率, 计算压枪倍率, 传入武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 载具
                    local adjusted_recoil = ceil_and_cache(recoil_data[2] * multiplier)    -- 调整后的后坐力, 向上取整并缓存小数部分, 乘以倍率
                    MoveMouseRelative(0, adjusted_recoil)    -- 移动鼠标相对位置, 传入0和调整后的后坐力
                    PressAndReleaseKey("F8")    -- 按下并释放按键, F8
                    if not IsMouseButtonPressed(1) then    -- 如果鼠标左键没有按下
                        break   -- 退出循环
                    end -- 如果鼠标左键按下, 则不做任何处理
                    if debugModeEnabled then     -- 如果启用了调试模式
                        MoveMouseRelative(2, 0)     -- 移动鼠标相对位置, 传入2和0
                    end -- 如果没有启用调试模式, 则不做任何处理
                    break   -- 退出循环
                end -- 如果压枪数据的子弹数不等于子弹数, 则不做任何处理
            end -- 遍历压枪数据结束

            Sleep(1)    -- 休眠1毫秒
        end -- 如果鼠标左键没有按下, 则不做任何处理
    elseif weaponBurstModes[weapon_name] then   -- 如果是burst模式

        while IsMouseButtonPressed(1) do    -- 如果鼠标左键按下
            if shoot == "None" then
                break
            end
            local ClickCurrentTime = GetRunningTime()    -- 当前时间
            bullet_count = math.ceil((ClickCurrentTime - ClickStartTime) / interval)    -- 子弹数, 向上取整, 传入当前时间和开始时间, 除以间隔

            for _, recoil_data in ipairs(pattern) do       -- 遍历压枪数据, recoil_data是压枪数据
                if recoil_data[1] == bullet_count then     -- 如果压枪数据的子弹数等于子弹数
                    multiplier = calculate_recoil_multiplier(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom,
                            car)     -- 压枪倍率, 计算压枪倍率, 传入武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 载具
                    local adjusted_recoil = ceil_and_cache(recoil_data[2] * multiplier)    -- 调整后的后坐力, 向上取整并缓存小数部分, 乘以倍率
                    MoveMouseRelative(0, adjusted_recoil)    -- 移动鼠标相对位置, 传入0和调整后的后坐力
                    if not IsMouseButtonPressed(1) then    -- 如果鼠标左键没有按下
                        break   -- 退出循环
                   end -- 如果鼠标左键按下, 则不做任何处理
                    if debugModeEnabled then     -- 如果启用了调试模式
                        MoveMouseRelative(2, 0)     -- 移动鼠标相对位置, 传入2和0
                    end -- 如果没有启用调试模式, 则不做任何处理
                    break   -- 退出循环
                end -- 如果压枪数据的子弹数不等于子弹数, 则不做任何处理
            end
            Sleep(1)
        end
    else

        while IsMouseButtonPressed(1) do    -- 如果鼠标左键按下
            if shoot == "None" then   -- 如果射击是None, 则退出循环
                break
            end

            local ClickCurrentTime = GetRunningTime()   -- 当前时间
            bullet_count = math.ceil((ClickCurrentTime - ClickStartTime) / interval)    -- 子弹数, 向上取整, 传入当前时间和开始时间, 除以间隔


            for _, recoil_data in ipairs(pattern) do    -- 遍历压枪数据, recoil_data是压枪数据
                if recoil_data[1] == bullet_count then  -- 如果压枪数据的子弹数等于子弹数

                    multiplier = calculate_recoil_multiplier(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, car)   -- 压枪倍率, 计算压枪倍率, 传入武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 载具
                    local adjusted_recoil = ceil_and_cache(recoil_data[2] * multiplier)   -- 调整后的后坐力, 向上取整并缓存小数部分, 乘以倍率
                    MoveMouseRelative(0, adjusted_recoil)   -- 移动鼠标相对位置, 传入0和调整后的后坐力
                    if not IsMouseButtonPressed(1) then  -- 如果鼠标左键没有按下
                        break   -- 退出循环
                    end
                end
            end

            Sleep(1)    -- 休眠1毫秒
        end
    end
end


local last_weapon_name = nil    -- 上一次的武器名
local last_muzzles = nil    -- 上一次的枪口
local last_grips = nil  -- 上一次的握把
local last_scopes = nil   -- 上一次的瞄准镜
local last_stocks = nil  -- 上一次的枪托
local last_poses = nil  -- 上一次的姿势
local last_shoot = nil  -- 上一次的射击

-- 以下是从文件中读取武器的函数, 用于读取武器信息
function read_weapon_from_file()    -- 从文件中读取武器
    if not is_authorized() then -- 如果没有授权
        return nil  -- 返回nil
    end
    weapon_name = nil
    scopes = nil
    muzzles = nil
    stocks= nil
    poses = nil
    shoot = nil
    car = nil

    dofile(addr)    -- 加载weapon.lua

    if weapon_name then -- 如果有武器名

        last_weapon_name = weapon_name
        last_muzzles = muzzles
        last_grips = grips
        last_scopes = scopes
        last_stocks = stocks
        last_poses = poses
        last_shoot = shoot
        last_car = car

        local output = string.format("%s+%s+%s+%s+%s+%s+%s+%s+%s",weapon_name, muzzles, grips, scopes, stocks, poses
        , scope_zoom, shoot, car)  -- 输出信息, 格式化字符串, 传入武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 射击, 载具
        OutputLogMessage("%s\n", output)        -- 输出信息, 传入信息
        return weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, shoot, car   -- 返回武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 射击, 载具
    else
        OutputLogMessage("未找到武器信息, 使用上一次的武器信息\n")

        return last_weapon_name, last_muzzles, last_grips, last_scopes, last_stocks, last_poses, last_scope_zoom, last_shoot, last_car  -- 返回上一次的武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 射击, 载具
    end
end

-- -------------->>> 以下是快速拾取函数 <<<--------------
function OnEvent(event, arg)    -- 事件处理函数, 传入事件和参数
    if event == "PROFILE_ACTIVATED" then        -- 如果事件是PROFILE_ACTIVATED
    elseif event == "PROFILE_DEACTIVATED" then  -- 如果事件是PROFILE_DEACTIVATED
        EnablePrimaryMouseButtonEvents(false)   -- 禁用主鼠标按钮事件
    elseif event == "MOUSE_BUTTON_PRESSED" then -- 如果事件是MOUSE_BUTTON_PRESSED
        if arg == 1 then    -- 如果参数是1
            ClickStartTime = GetRunningTime()   -- 开始射击时间, 获取当前时间
            PressKey("F8")  -- 按下按键, F8
            local weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, shoot, car = read_weapon_from_file()  -- 从文件中读取武器信息
            if not scope_zoom then  -- 如果没有瞄准倍率
                scope_zoom = 1 -- 使用默认值 1
            end

            if weapon_name then -- 如果有武器名
                apply_recoil(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, shoot, car)    -- 应用压枪, 传入武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 射击, 载具
            end

        elseif arg == 2 then    -- 如果参数是2
            local weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, shoot, car = read_weapon_from_file()  -- 从文件中读取武器信息
            if weapon_name then -- 如果有武器名
                local output = string.format("%s+%s+%s+%s+%s+%s+%s+%s",weapon_name, muzzles, grips, scopes, stocks, poses , scope_zoom, shoot, car) -- 输出信息, 格式化字符串, 传入武器名, 枪口, 握把, 瞄准镜, 枪托, 姿势, 瞄准倍率, 射击, 载具
                OutputLogMessage("%s\n", output)
            end

        elseif arg == 5 and IsModifierPressed("lctrl") then -- 如果参数是5并且按下了左ctrl键
            local weapon_name = read_weapon_from_file() -- 从文件中读取武器信息
            if weapon_name then -- 如果有武器名
                weaponBurstModes[weapon_name] = not weaponBurstModes[weapon_name]   -- 武器burst模式, 取反
                OutputLogMessage("weapon %s tutuut %s\n", weapon_name, weaponBurstModes[weapon_name] and "on" or "close")   -- 输出信息, 传入武器名和是否开启
            end
        elseif arg == 4 and IsModifierPressed("lctrl") then -- 如果参数是4并且按下了左ctrl键
            debugModeEnabled = not debugModeEnabled  -- 调试模式, 取反
            OutputLogMessage("debug%s\n", debugModeEnabled and "on" or "close")  -- 输出信息, 传入是否开启
        elseif arg == 9 then    -- 如果参数是9
            fastPickup()    -- 快速拾取
        end
    elseif event == "MOUSE_BUTTON_RELEASED" then    -- 如果事件是MOUSE_BUTTON_RELEASED
        if arg == 1 then    -- 如果参数是1
            ReleaseKey("F8")    -- 释放按键, F8
            MoveMouseRelative(0, 0)   -- 移动鼠标相对位置, 传入0和0
        end
    end

    if (event == "MOUSE_BUTTON_PRESSED" and arg == pick and IsModifierPressed("lctrl")) then    -- 如果事件是MOUSE_BUTTON_PRESSED并且参数是pick并且按下了左ctrl键
        autopick()  -- 自动拾取
    end
end

pick = 3    -- 拾取

autopick = function()   -- 自动拾取
    PressAndReleaseKey("tab")   -- 按下并释放按键, tab
    Sleep(1)    -- 休眠1毫秒
    for k=1,10 do   -- 循环10次
        for j=1,5 do    -- 循环5次
            MoveMouseTo(7800, (35000 - j * 5425))   -- 移动鼠标到, 7800和(35000 - j * 5425)
            PressMouseButton(1) -- 按下鼠标按钮, 1
            MoveMouseTo(32767 + j * 11, 12500 + j * 12)  -- 移动鼠标到, 32767 + j * 11和12500 + j * 12
            ReleaseMouseButton(1)   -- 释放鼠标按钮, 1
            Sleep(1)    -- 休眠1毫秒
        end
    end
    MoveMouseTo(32767, 32767)   -- 移动鼠标到, 32767和32767
    Sleep(1)    -- 休眠1毫秒
    PressAndReleaseKey("tab")   -- 按下并释放按键, tab
end

function G1_PRESSED() G1___ = true OnEvent("MOUSE_BUTTON_PRESSED",1,"mouse") end    -- G1按下, G1___为true, 调用OnEvent函数, 传入MOUSE_BUTTON_PRESSED,1和mouse
function G1_RELEASED() G1___ = false OnEvent("MOUSE_BUTTON_RELEASED",1,"mouse") end -- G1释放, G1___为false, 调用OnEvent函数, 传入MOUSE_BUTTON_RELEASED,1和mouse
function G2_PRESSED() G2___ = true OnEvent("MOUSE_BUTTON_PRESSED",2,"mouse") end    -- G2按下, G2___为true, 调用OnEvent函数, 传入MOUSE_BUTTON_PRESSED,2和mouse
function G2_RELEASED() G2___ = false OnEvent("MOUSE_BUTTON_RELEASED",2,"mouse") end -- G2释放, G2___为false, 调用OnEvent函数, 传入MOUSE_BUTTON_RELEASED,2和mouse
function G3_PRESSED() G3___ = true OnEvent("MOUSE_BUTTON_PRESSED",3,"mouse") end    -- G3按下, G3___为true, 调用OnEvent函数, 传入MOUSE_BUTTON_PRESSED,3和mouse
function G3_RELEASED() G3___ = false OnEvent("MOUSE_BUTTON_RELEASED",3,"mouse") end -- G3释放, G3___为false, 调用OnEvent函数, 传入MOUSE_BUTTON_RELEASED,3和mouse
function G4_PRESSED() G4___ = true OnEvent("MOUSE_BUTTON_PRESSED",4,"mouse") end    -- G4按下, G4___为true, 调用OnEvent函数, 传入MOUSE_BUTTON_PRESSED,4和mouse
function G4_RELEASED() G4___ = false OnEvent("MOUSE_BUTTON_RELEASED",4,"mouse") end -- G4释放, G4___为false, 调用OnEvent函数, 传入MOUSE_BUTTON_RELEASED,4和mouse
function G5_PRESSED() G5___ = true OnEvent("MOUSE_BUTTON_PRESSED",5,"mouse") end    -- G5按下, G5___为true, 调用OnEvent函数, 传入MOUSE_BUTTON_PRESSED,5和mouse
function G5_RELEASED() G5___ = false OnEvent("MOUSE_BUTTON_RELEASED",5,"mouse") end -- G5释放, G5___为false, 调用OnEvent函数, 传入MOUSE_BUTTON_RELEASED,5和mouse
while true do
  while IsMouseButtonPressed(1) and not G1___ do G1_PRESSED() break Sleep(1) end    -- 如果鼠标左键按下并且G1___为false, 则调用G1_PRESSED函数, 传入1, 休眠1毫秒
  while not IsMouseButtonPressed(1) and G1___ do G1_RELEASED() break Sleep(1)end    -- 如果鼠标左键没有按下并且G1___为true, 则调用G1_RELEASED函数, 传入1, 休眠1毫秒
  while IsMouseButtonPressed(3) and not G2___ do G2_PRESSED() break Sleep(1) end    -- 如果鼠标右键按下并且G2___为false, 则调用G2_PRESSED函数, 传入2, 休眠1毫秒
  while not IsMouseButtonPressed(3) and G2___ do G2_RELEASED() break Sleep(1)end    -- 如果鼠标右键没有按下并且G2___为true, 则调用G2_RELEASED函数, 传入2, 休眠1毫秒
  while IsMouseButtonPressed(2) and not G3___ do G3_PRESSED() break Sleep(1) end    -- 如果鼠标中键按下并且G3___为false, 则调用G3_PRESSED函数, 传入3, 休眠1毫秒
  while not IsMouseButtonPressed(2) and G3___ do G3_RELEASED() break Sleep(1)end    -- 如果鼠标中键没有按下并且G3___为true, 则调用G3_RELEASED函数, 传入3, 休眠1毫秒
  while IsMouseButtonPressed(4) and not G4___ do G4_PRESSED() break Sleep(1) end    -- 如果鼠标4键按下并且G4___为false, 则调用G4_PRESSED函数, 传入4, 休眠1毫秒
  while not IsMouseButtonPressed(4) and G4___ do G4_RELEASED() break Sleep(1)end    -- 如果鼠标4键没有按下并且G4___为true, 则调用G4_RELEASED函数, 传入4, 休眠1毫秒
  while IsMouseButtonPressed(5) and not G5___ do G5_PRESSED() break Sleep(1) end    -- 如果鼠标5键按下并且G5___为false, 则调用G5_PRESSED函数, 传入5, 休眠1毫秒
  while not IsMouseButtonPressed(5) and G5___ do G5_RELEASED() break Sleep(1)end    -- 如果鼠标5键没有按下并且G5___为true, 则调用G5_RELEASED函数, 传入5, 休眠1毫秒
  Sleep(1)
end


