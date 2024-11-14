EnablePrimaryMouseButtonEvents(true)

-- 定义武器配件的修正系数
local attachment_multipliers = {
    poses = {
        None = 1,
        stand = 1,
        down = 0.83,
    },
    muzzles_rifle = {
        None = 1,
        bc2 = 0.79,
        bc1 = 0.79,
        xx = 1,
        xy1 = 0.855,
        xy2 = 0.855,
    },
    grips_rifle = {
        None = 3,
        angle = 1,
        light = 0.85,
        line = 0.792,
        red = 0.83,
        thumb = 0.9,
    },
    scopes_rifle = {
        None = 1,
        reddot = 1,
        quanxi = 1,
        x2 = 1.24,
        x3 = 1.65,
        x4 = 2.2,
        x6 = 1.65,
        x8 = 0.9,
    },
    stocks_rifle = {
        None = 1,
        heavy = 1,
        normal = 1,
    },
    muzzles_sniper = {
        None = 1,
    },
    grips_sniper = {
        None = 1,
    },
    scopes_sniper = {
        None = 1,
        x8 = 1,
    },
    stocks_sniper = {
        None = 1,
    }
}

-- 预定义武器的压枪模式（每个数组元素表示一发子弹的压枪力度）
local recoil_patterns = {
    Berry = {
    {1, 50}, 
    {2, 50}, 
    {3, 50}, 
    {4, 50},
    {5, 50}, 
    {6, 50},
    {7, 50}, 
    {8, 50},
    {9, 50}, 
    {10, 50},
    {11, 50}, 
    {12, 50}, 
    {13, 50}, 
    {14, 50},
    {15, 50}, 
    {16, 50},
    {17, 50}, 
    {18, 50},
    {19, 50}, 
    {20, 50},
    {21, 50}, 
    {22, 50}, 
    {23, 50}, 
    {24, 50},
    {25, 50}, 
    {26, 50},
    {27, 50}, 
    {28, 50},
    {29, 50}, 
    {30, 80},
    {31, 80}, 
    {32, 80}, 
    {33, 80}, 
    {34, 80},
    {35, 80}, 
    {36, 80},
    {37, 80}, 
    {38, 80},
    {39, 80}, 
    {40, 80},
    },  -- 4发子弹的压枪模式
    AUG = {{1, 10}, {2, 10}, {3, 10}, {4, 10}},   -- 4发子弹的压枪模式
    MK47 = {
    {1, 5}, 
    {2, 5}, 
    {3, 5}, 
    {4, 5},
    {5, 5}, 
    {6, 5},
    {7, 5}, 
    {8, 5},
    {9, 5}, 
    {10, 5},
    },  -- 4发子弹的压枪模式
    M16 = {{1, 10}, {2, 10}, {3, 10}, {4, 10}},   -- 4发子弹的压枪模式
    SKS = {{1, 60}, {2, 60}, {3, 60}, {4, 60}},  -- 4发子弹的压枪模式
}

-- 定义武器射击间隔
local weapon_intervals = {
    Berry =75,
    AUG = 100,
    MK47 = 400,
    M16 = 100,
    SKS = 100,
}

-- 累计小数部分
local decimal_cache = 0

-- 向上取整并缓存小数部分
function ceil_and_cache(value)
    local integer_part = math.floor(value)
    decimal_cache = decimal_cache + value - integer_part
    if decimal_cache >= 1 then
        integer_part = integer_part + 1
        decimal_cache = decimal_cache - 1
    end
    return integer_part
end

-- 计算修正系数
function calculate_recoil_multiplier(poses, muzzles, grips, scopes, stocks, weapon_type)
    local multiplier = 1

    multiplier = multiplier * (attachment_multipliers["muzzles_"..weapon_type][muzzles] or 1)
    multiplier = multiplier * (attachment_multipliers["grips_"..weapon_type][grips] or 1)
    multiplier = multiplier * (attachment_multipliers["scopes_"..weapon_type][scopes] or 1)
    multiplier = multiplier * (attachment_multipliers["stocks_"..weapon_type][stocks] or 1)
    multiplier = multiplier * (attachment_multipliers.poses[poses] or 1)

    if IsModifierPressed("ralt") then
        multiplier = multiplier * (attachment_multipliers.poses.down or 1)
    end

    return multiplier
end

-- 定义全局变量来控制非 MK47/M16 枪械的连点模式
local burstModeEnabled = false

-- 应用压枪
function apply_recoil(weapon_name, muzzles, grips, scopes, stocks, weapon_type)
    local pattern = recoil_patterns[weapon_name]
    local interval = weapon_intervals[weapon_name]
    if not pattern then
        OutputLogMessage("未找到武器的压枪参数: %s\n", weapon_name)
        return
    end

    local multiplier = calculate_recoil_multiplier(poses, muzzles, grips, scopes, stocks, weapon_type)
    local bullet_count = 0

    if weapon_name == "MK47" or weapon_name == "M16" then
        -- MK47 和 M16 特殊处理
        local isFirstClick = true
        for i, recoil_data in ipairs(pattern) do
            if IsMouseButtonPressed(3) or IsMouseButtonPressed(4)then
                bullet_count = bullet_count + 1
                if bullet_count == recoil_data[1] then
                    local adjusted_recoil = ceil_and_cache(recoil_data[2] * multiplier)
                    MoveMouseRelative(0, adjusted_recoil)
                    Sleep(interval) 
                     PressAndReleaseMouseButton(1)                   
            end  
        end   
    end          
           
    elseif burstModeEnabled then 
        -- 其他枪械在开启连点模式后才进行连点压枪
        for i, recoil_data in ipairs(pattern) do
            if IsMouseButtonPressed(3) then
                bullet_count = bullet_count + 1
                if bullet_count == recoil_data[1] then
                    local adjusted_recoil = ceil_and_cache(recoil_data[2] * multiplier)
                    MoveMouseRelative(0, adjusted_recoil)
                    Sleep(interval)
                    PressAndReleaseMouseButton(1)  -- 连点
                end
            else
                break
            end
        end        
    else
        -- 其他枪械的默认压枪处理（不连点）
        for i, recoil_data in ipairs(pattern) do
            if IsMouseButtonPressed(3) then
                bullet_count = bullet_count + 1
                if bullet_count == recoil_data[1] then
                    local adjusted_recoil = ceil_and_cache(recoil_data[2] * multiplier)
                    MoveMouseRelative(0, adjusted_recoil)
                    Sleep(interval)
                    if not IsMouseButtonPressed(1) then
                        break
                    end
                end
            else
                break
            end
        end
    end
end

-- 读取武器信息
function read_weapon_from_file()
    -- 清除之前的武器信息
    weapon_name_rifle, weapon_name_sniper = nil, nil
    muzzles_rifle, grips_rifle, scopes_rifle, stocks_rifle = nil, nil, nil, nil
    muzzles_sniper, grips_sniper, scopes_sniper, stocks_sniper = nil, nil, nil, nil

    -- 读取新的武器信息
    dofile("C:/Users/38936/Desktop/Temp/weapon.lua")

    if weapon_name_rifle then
        local output = weapon_name_rifle .. "+" .. muzzles_rifle .. "+" .. grips_rifle .. "+" .. scopes_rifle .. "+" .. stocks_rifle
        OutputLogMessage("%s\n", output)
        return weapon_name_rifle, muzzles_rifle, grips_rifle, scopes_rifle, stocks_rifle, "rifle"
    elseif weapon_name_sniper then
        local output = weapon_name_sniper .. "+" .. muzzles_sniper .. "+" .. grips_sniper .. "+" .. scopes_sniper .. "+" .. stocks_sniper
        OutputLogMessage("%s\n", output)
        return weapon_name_sniper, muzzles_sniper, grips_sniper, scopes_sniper, stocks_sniper, "sniper"
    else
        OutputLogMessage("未找到武器信息\n")
        return nil, nil, nil, nil, nil, nil
    end
end

-- 事件处理函数
function OnEvent(event, arg)
    if event == "MOUSE_BUTTON_PRESSED" then
        local weapon_name, muzzles, grips, scopes, stocks, weapon_type = read_weapon_from_file()
        if arg == 1 and (IsMouseButtonPressed(3) or IsMouseButtonPressed(4)) then
            apply_recoil(weapon_name, muzzles, grips, scopes, stocks, weapon_type)
        end
    elseif event == "MOUSE_BUTTON_RELEASED" and arg == 1 then
        MoveMouseRelative(0, 0)
        continueClicking = false
    elseif event == "MOUSE_BUTTON_RELEASED" and (arg == 3 or arg == 4) then
        continueClicking = false
    end

 if event == "MOUSE_BUTTON_PRESSED" and arg == 5 and IsModifierPressed("lctrl") then
        burstModeEnabled = not burstModeEnabled  -- 切换连点模式
        if burstModeEnabled then
            OutputLogMessage("连点模式已开启\n")
        else
            OutputLogMessage("连点模式已关闭\n")
        end
    end
    if event == "MOUSE_BUTTON_PRESSED" then
        if IsModifierPressed("ralt") then
            OutputLogMessage("右alt键被按下!\n")
        end
    elseif event == "MOUSE_BUTTON_RELEASED" then
        if IsModifierPressed("ralt") then
            OutputLogMessage("右alt键被松开!\n")
        end
    end
end