EnablePrimaryMouseButtonEvents(true)

local file_address = "F:/Object/GitHub/CuteAide/output.lua"


local decimal_cache = 0 -- 用于缓存小数部分，以便在下一次调用时使用

-- 以下是向上取整并缓存小数部分的函数
function ceil_and_cache(value)
    local integer_part = math.floor(value)
    decimal_cache = decimal_cache + value - integer_part
    if decimal_cache >= 1 then
        integer_part = integer_part + 1
        decimal_cache = decimal_cache - 1
    end
    return integer_part
end

-- 判断是否授权
local function is_authorized()
    local success, chunk = pcall(dofile, file_address)
    if not success then
        OutputLogMessage("读取文件报错 weapon.lua: %s\n", chunk)
        return false
    end
        return true
end

-- 计算后坐力
function calculate_influencing_factor(scope, muzzle, grip, stock, car, posture_state, in_car, alone_factor,
                                      global_lshift,global_recoil)
    calculation_results = scope * muzzle * grip * stock * posture_state * alone_factor * global_recoil
    if in_car == "yes" then   -- 在车上
        calculation_results = calculation_results * car
    end

    if IsModifierPressed("lshift") then  -- 按住左shift
        calculation_results = calculation_results * global_lshift
    end
    return calculation_results
end

local start_shooting_time = 0 -- 开始射击时间

-- 开始压枪
function pressure_grab(weapon, scope, muzzle, grip, stock, car,posture_state, in_car, guns_trajectory,
                       weapon_intervals,shooting_state,opening_method,continuous_clicks,alone_factor, global_lshift,
                       global_recoil)
    if not is_authorized() then
        return
    end

    if weapon == nil or weapon == "weapon_none" then
        OutputLogMessage("请先读取武器参数或当前武器为 weapon_none \n")
        return
    end

    local _trajectory = guns_trajectory -- 枪械轨迹
    local _intervals = weapon_intervals  -- 武器间隔
    local total_coefficient = calculate_influencing_factor(scope, muzzle, grip, stock, car, posture_state, in_car, alone_factor, global_lshift,global_recoil)    -- 总系数

    local _number_bullets = 0   -- 子弹数

    local _special_weapon = {MK47=true, M16A4=true, MINI14=true, SKS=true, MK12=true, ZDZT=true,QBU=true}  -- 特殊武器
    OutputLogMessage("当前武器: %s ,  --->>  影响因子为: %.2f\n", weapon, total_coefficient)
    if _special_weapon[weapon] then
        while IsMouseButtonPressed(1) do
            local current_click_time = GetRunningTime() -- 当前点击时间
            _number_bullets = math.ceil((current_click_time - start_shooting_time) / _intervals)  -- 子弹数

            if shooting_state == "stop" then    -- 停止射击
                break
            end

            if opening_method == "click" then   -- 点击开镜
                if continuous_clicks == "open" then
                    enable_mouse_events = false  -- 禁用鼠标事件
                    for _,recoil_data in ipairs(_trajectory) do
                        if recoil_data[1] == _number_bullets then
                            total_coefficient = calculate_influencing_factor(scope, muzzle, grip, stock, car, posture_state, in_car, alone_factor,global_lshift,global_recoil)

                            local adjusted_recoil = ceil_and_cache(recoil_data[2] * total_coefficient)
                            MoveMouseRelative(0, adjusted_recoil)
                            if not IsMouseButtonPressed(1) then
                                break
                            end
                            break
                        end
                    end
                    enable_mouse_events = true  -- 启用鼠标事件
                end
            elseif opening_method == "long_press" then  -- 长按开镜
                if IsMouseButtonPressed(3) or IsMouseButtonPressed(4) then
                    if continuous_clicks == "open" then
                        enable_mouse_events = false  -- 禁用鼠标事件
                        for _,recoil_data in ipairs(_trajectory) do
                            if recoil_data[1] == _number_bullets then
                                total_coefficient = calculate_influencing_factor(scope, muzzle, grip, stock, car, posture_state, in_car, alone_factor, global_lshift,global_recoil)
                                local adjusted_recoil = ceil_and_cache(recoil_data[2] * total_coefficient)

                                MoveMouseRelative(0, adjusted_recoil)

                                if not IsMouseButtonPressed(1) then
                                    break
                                end
                                break
                            end
                        end
                        enable_mouse_events = true  -- 启用鼠标事件
                    end
                end
            end
            Sleep(1)
        end
    else
        while IsMouseButtonPressed(1) do
            if shooting_state == "stop" then    -- 停止射击
                break
            end

            local current_click_time = GetRunningTime() -- 当前点击时间
            _number_bullets = math.ceil((current_click_time - start_shooting_time) / _intervals)  -- 子弹数

            if opening_method == "click" then   -- 点击开镜
                for _,recoil_data in ipairs(_trajectory) do
                    if recoil_data[1] == _number_bullets then
                        total_coefficient = calculate_influencing_factor(scope, muzzle, grip, stock, car, posture_state, in_car, alone_factor,global_lshift,global_recoil)

                        local adjusted_recoil = ceil_and_cache(recoil_data[2] * total_coefficient)
                        MoveMouseRelative(0, adjusted_recoil)
                        if not IsMouseButtonPressed(1) then
                            break
                        end
                        break
                    end
                end
                Sleep(1)

            elseif opening_method == "long_press" then  -- 长按开镜
                if IsMouseButtonPressed(3) or IsMouseButtonPressed(4) then
                    for _,recoil_data in ipairs(_trajectory) do
                        if recoil_data[1] == _number_bullets then
                            total_coefficient = calculate_influencing_factor()
                            local adjusted_recoil = ceil_and_cache(recoil_data[2] * total_coefficient)

                            MoveMouseRelative(0, adjusted_recoil)
                            if not IsMouseButtonPressed(1) then
                                break
                            end
                            break
                        end
                    end
                end
            end
            Sleep(1)
        end
    end
end

-- 从文件中读取武器
function read_weapon_from_file()
    if not is_authorized() then
        return
    end
    local weapon_name = nil
    dofile(file_address)
    weapon_name = weapon
    OutputLogMessage("当前武器: %s, 倍镜: %.2f, 枪口: %.2f, 握把: %.2f, 枪托: %.2f\n", weapon_name, scope, muzzle, grip, stock)
    return weapon_name, scope, muzzle, grip, stock, car, posture_state, in_car, guns_trajectory, weapon_intervals, shooting_state, opening_method, continuous_clicks, alone_factor, global_lshift, global_recoil
end


-- 事件处理
function event_handing(event, key)
    if event == "mouse_button_down" then
        if key == 1 then
            start_shooting_time = GetRunningTime()
            local weapon, scope, muzzle, grip, stock, car, posture_state, in_car, guns_trajectory, weapon_intervals, shooting_state, opening_method, continuous_clicks, alone_factor, global_lshift, global_recoil = read_weapon_from_file()
            pressure_grab(weapon, scope, muzzle, grip, stock, car, posture_state, in_car, guns_trajectory, weapon_intervals, shooting_state, opening_method, continuous_clicks, alone_factor, global_lshift, global_recoil)
        elseif key == 2 then
            OutputLogMessage("右键按下\n")
        end
    elseif event == "mouse_button_up" then
        if key == 1 then
            ReleaseKey("F8")
            MoveMouseRelative(0, 0)
        end
    end
    if (event == "mouse_button_down" and key == pick and IsModifierPressed("lctrl")) then    -- 如果事件是MOUSE_BUTTON_PRESSED并且参数是pick并且按下了左ctrl键
        auto_pick()  -- 自动拾取
    end
end

pick = 3    -- 拾取

auto_pick = function()   -- 自动拾取
    PressAndReleaseKey("tab")
    Sleep(1)
    for k=1,10 do
        for j=1,5 do
            MoveMouseTo(7800, (35000 - j * 5425))
            PressMouseButton(1)
            MoveMouseTo(32767 + j * 11, 12500 + j * 12)
            ReleaseMouseButton(1)
            Sleep(1)
        end
    end
    MoveMouseTo(32767, 32767)
    Sleep(1)
    PressAndReleaseKey("tab")
end

local enable_mouse_events = true

function g1_down() if enable_mouse_events then g1___ = true event_handing("mouse_button_down", 1, "mouse") end end
function g1_up() if enable_mouse_events then g1___ = false event_handing("mouse_button_up", 1, "mouse") end end
function g2_down() if enable_mouse_events then g2___ = true event_handing("mouse_button_down", 2, "mouse") end end
function g2_up() if enable_mouse_events then g2___ = false event_handing("mouse_button_up", 2, "mouse") end end
function g3_down() if enable_mouse_events then g3___ = true event_handing("mouse_button_down", 3, "mouse") end end
function g3_up() if enable_mouse_events then g3___ = false event_handing("mouse_button_up", 3, "mouse") end end
function g4_down() if enable_mouse_events then g4___ = true event_handing("mouse_button_down", 4, "mouse") end end
function g4_up() if enable_mouse_events then g4___ = false event_handing("mouse_button_up", 4, "mouse") end end
function g5_down() if enable_mouse_events then g5___ = true event_handing("mouse_button_down", 5, "mouse") end end
function g5_up() if enable_mouse_events then g5___ = false event_handing("mouse_button_up", 5, "mouse") end end

while true do
  while IsMouseButtonPressed(1) and not g1___ do g1_down() break Sleep(1) end
  while not IsMouseButtonPressed(1) and g1___ do g1_up() break Sleep(1)end
  while IsMouseButtonPressed(3) and not g2___ do g2_down() break Sleep(1) end
  while not IsMouseButtonPressed(3) and g2___ do g2_up() break Sleep(1)end
  while IsMouseButtonPressed(2) and not g3___ do g3_down() break Sleep(1) end
  while not IsMouseButtonPressed(2) and g3___ do g3_up() break Sleep(1)end
  while IsMouseButtonPressed(4) and not g4___ do g4_down() break Sleep(1) end
  while not IsMouseButtonPressed(4) and g4___ do g4_up() break Sleep(1)end
  while IsMouseButtonPressed(5) and not g5___ do g5_down() break Sleep(1) end
  while not IsMouseButtonPressed(5) and g5___ do g5_up() break Sleep(1)end
  Sleep(10)
end