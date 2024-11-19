dofile("C:/PUBG/Config/Plugins.lua")

-- 弹道调试 | false不显示，true显示
Ballistic = false
-- 压枪键 | 单点开镜设置：false 、长按开机设置：true
DownGun = true
-- 1号枪和2号枪切换
Convert = 4

random = function(m, n)
    local mean = (m + n) / 2
    local sigma = (n - m) / (2 * 1.645)
    local u1 = math.random()
    local u2 = math.random()
    local z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    local dao_mai_sha_bi = math.floor(mean + z0 * sigma + 0.5)
    while dao_mai_sha_bi < m do
        dao_mai_sha_bi = math.random(m, n)
    end
    return dao_mai_sha_bi
end

delay = function(wait)
    -- 延迟函数
    local nowTime = GetRunningTime()    -- 获取当前时间
    while GetRunningTime() - nowTime <= wait do
        -- 当前时间减去开始时间小于等于延迟时间
    end
end
Auto_Down = function()
    if (Ballistic == true and IsMouseButtonPressed(1)) then
        ClearLog()
    end
    local nowTime = GetRunningTime()
    local bulletIndex = 0   -- 子弹数
    for i = 1, #Gun.bullet do
        while IsMouseButtonPressed(1) and bulletIndex <= Gun.bullet[i] do
            MoveMouseRelative(0, math.floor(Gun.Downforce[i]))
            if Ballistic then
                OutputLogMessage("弹道：%s : %sn", bulletIndex, Gun.Downforce[i])
            end
            delay(math.floor(random((Gun.interval - 10), (Gun.interval + 10)) / 4 + 0.5))
            bulletIndex = tonumber(string.format("%.2f", (GetRunningTime() - nowTime) / Gun.interval + 0.5))
        end
    end
end

function OnEvent(event, arg)
    if (event == "MOUSE_BUTTON_RELEASED" and arg == Convert) then
        --  1号枪和2号枪切换
        Gunseat = not Gunseat   -- 1号枪和2号枪切换
        if Gunseat then
            -- 1号枪
            PressAndReleaseKey("2") -- 2号枪
        else
            PressAndReleaseKey("1") -- 1号枪
        end
    elseif (event == "MOUSE_BUTTON_PRESSED" and arg == 1) then
        -- 鼠标左键,压枪
        if (Ballistic == true) then
            dofile("C:/PUBG/Config/Plugins.lua")
        end
        dofile("C:/PUBG/Config/Guninfo.lua")
        if IsMouseButtonPressed(3) and DownGun == true then
            delay(27)
            Auto_Down()
        elseif (click == true and DownGun == false) then
            delay(27)
            Auto_Down()
        end
    elseif (event == "MOUSE_BUTTON_RELEASED" and arg == 2) then
        click = not click
    elseif (event == "MOUSE_BUTTON_RELEASED" and arg == 1) then
        click = false
    end
end
ClearLog()
OutputLogMessage("%sn", "运行成功")
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