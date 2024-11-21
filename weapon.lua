address = "C:/CuteAide/output.lua"

-- 计算后坐力
function calculate_influencing_factor()
    dofile(address)
    calculation_results = coefficient
    if in_car == "yes" then
        -- 在车上
        calculation_results = calculation_results * car
    end

    if IsModifierPressed("lshift") then
        -- 按住左shift
        calculation_results = calculation_results * global_lshift
    end
    return calculation_results
end

local debug = false

-- 开始压枪
Auto_Down = function()
    dofile(address)
    ClearLog()
    if coefficient == "none" then
        OutputLogMessage("当前武器不支持压枪: %s\n", weapon)
        return
    end
    if weapon == nil or weapon == "weapon_none" then
        OutputLogMessage("请先读取武器参数或当前武器为 weapon_none \n")
        return
    end

    --decimal_cache = 0
    --
    --function ceil_and_cache(value)
    --    integer_part = math.floor(value)
    --    decimal_cache = decimal_cache + value - integer_part
    --    if decimal_cache >= 1 then
    --        integer_part = integer_part + 1
    --        decimal_cache = decimal_cache - 1
    --    end
    --    return integer_part
    --end

    _number_bullets = 0   -- 子弹数
    nowTime = GetRunningTime()
    last_logged_bullet = 0  -- 记录最后输出的子弹数

    while IsMouseButtonPressed(1) do
        if shooting_state == "stop" then
            break
        end

        _number_bullets = math.ceil((GetRunningTime() - nowTime) / weapon_intervals)  -- 子弹数

        for _, recoil_data in ipairs(guns_trajectory) do
            if recoil_data[1] == _number_bullets then
                adjusted_recoil = math.floor(recoil_data[2] * calculate_influencing_factor())  -- 调整后的后坐力
                -- 只在新子弹发射时输出日志
                if _number_bullets > last_logged_bullet then
                    OutputLogMessage("当前子弹数: %s, 后坐力: %s, 系数: %s, 下压像素: %s\n",
                                     _number_bullets, recoil_data[2],
                                     calculate_influencing_factor(), adjusted_recoil)
                    last_logged_bullet = _number_bullets  -- 更新最后输出的子弹数
                end
                MoveMouseRelative(0, adjusted_recoil)
                if not IsMouseButtonPressed(1) then
                    break
                end
                if debug then
                    MoveMouseRelative(1, 0)
                end
                Sleep(10)
            end
        end
    end
end

delay = function(wait)
    -- 延迟函数
    local nowTime = GetRunningTime()    -- 获取当前时间
    while GetRunningTime() - nowTime <= wait do
        -- 当前时间减去开始时间小于等于延迟时间
    end
end


-- 事件处理
function OnEvent(event, key)
    dofile(address)

    if event == "MOUSE_BUTTON_PRESSED" and key == 1 then

        if opening_method == "click" then
            -- 点击开镜
            delay(27)
            Auto_Down()
        elseif opening_method == "long_press" and IsMouseButtonPressed(3) then
            -- 长按开镜
            delay(27)
            Auto_Down()
        end
    end
end

ClearLog()
OutputLogMessage("%s", "运行成功\n")
EnablePrimaryMouseButtonEvents(true)
math.randomseed(GetDate("%H%M%S"):reverse())

function G1_PRESSED()
    G1___ = true
    OnEvent("MOUSE_BUTTON_PRESSED", 1, "mouse")
end
function G1_RELEASED()
    G1___ = false
    OnEvent("MOUSE_BUTTON_RELEASED", 1, "mouse")
end
function G2_PRESSED()
    G2___ = true
    OnEvent("MOUSE_BUTTON_PRESSED", 2, "mouse")
end
function G2_RELEASED()
    G2___ = false
    OnEvent("MOUSE_BUTTON_RELEASED", 2, "mouse")
end
function G3_PRESSED()
    G3___ = true
    OnEvent("MOUSE_BUTTON_PRESSED", 3, "mouse")
end
function G3_RELEASED()
    G3___ = false
    OnEvent("MOUSE_BUTTON_RELEASED", 3, "mouse")
end
function G4_PRESSED()
    G4___ = true
    OnEvent("MOUSE_BUTTON_PRESSED", 4, "mouse")
end
function G4_RELEASED()
    G4___ = false
    OnEvent("MOUSE_BUTTON_RELEASED", 4, "mouse")
end
function G5_PRESSED()
    G5___ = true
    OnEvent("MOUSE_BUTTON_PRESSED", 5, "mouse")
end
function G5_RELEASED()
    G5___ = false
    OnEvent("MOUSE_BUTTON_RELEASED", 5, "mouse")
end
while true do
    while IsMouseButtonPressed(1) and not G1___ do
        G1_PRESSED()
        break
        Sleep(1)
    end
    while not IsMouseButtonPressed(1) and G1___ do
        G1_RELEASED()
        break
        Sleep(1)
    end
    while IsMouseButtonPressed(3) and not G2___ do
        G2_PRESSED()
        break
        Sleep(1)
    end
    while not IsMouseButtonPressed(3) and G2___ do
        G2_RELEASED()
        break
        Sleep(1)
    end
    while IsMouseButtonPressed(2) and not G3___ do
        G3_PRESSED()
        break
        Sleep(1)
    end
    while not IsMouseButtonPressed(2) and G3___ do
        G3_RELEASED()
        break
        Sleep(1)
    end
    while IsMouseButtonPressed(4) and not G4___ do
        G4_PRESSED()
        break
        Sleep(1)
    end
    while not IsMouseButtonPressed(4) and G4___ do
        G4_RELEASED()
        break
        Sleep(1)
    end
    while IsMouseButtonPressed(5) and not G5___ do
        G5_PRESSED()
        break
        Sleep(1)
    end
    while not IsMouseButtonPressed(5) and G5___ do
        G5_RELEASED()
        break
        Sleep(1)
    end
    Sleep(1)
end