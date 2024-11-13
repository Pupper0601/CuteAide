
local file_address = "F:/Object/GitHub/CuteAide/output.lua"

-- 判断是否授权
local function is_authorized()
    local success, chunk = pcall(dofile, file_address)
    if not success then
        OutputLogMessage("Error loading weapon.lua: %s\n", chunk)
        return false
    end
        return true
end

-- 读取文件
function read_file()
    if not is_authorized() then
        return  nil
    end
    _config = dofile(file_address)
end

-- 计算后坐力
function calculate_influencing_factor()
    if not _config then
        read_file()
    end
    calculation_results = _config.scope * _config.muzzle * _config.grip * _config.stock * _config.posture_state * _config.alone_factor * _config.global_recoil
    if _config.in_car == 1 then   -- 在车上
        calculation_results = calculation_results * _config.car
    end

    if IsModifierPressed("lshift") then  -- 按住左shift
        calculation_results = calculation_results * _config.global_lshift
    end
    return calculation_results
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



local start_shooting_time = 0 -- 开始射击时间

-- 开始压枪
function pressure_grab()
    if not _config then
        read_file()
    end
    local _trajectory = _config.guns_trajectory -- 枪械轨迹
    local _intervals = _config.weapon_intervals  -- 武器间隔
    local total_coefficient = calculate_influencing_factor()    -- 总系数
    local _number_bullets = 0   -- 子弹数

    local _special_weapon = {MK47=true, M16A4=true, MINI14=true, SKS=true, MK12=true, ZDZT=true,QBU=true}  -- 特殊武器

    if _special_weapon[_trajectory] then
        while IsMouseButtonPressed(1) do
            if _config.shooting_state == "stop" then    -- 停止射击
                break
            end

            local current_click_time = GetRunningTime() -- 当前点击时间
            bullet_count = math.ceil((current_click_time - start_shooting_time) / _intervals)  -- 子弹数

            for _,recoil_data in ipairs(_config.recoil) do
                if recoil_data[1] == bullet_count then
                    total_coefficient = calculate_influencing_factor()
                    local adjusted_recoil = ceil_and_cache(recoil_data[2] * total_coefficient)
                    MoveMouseRelative(0, adjusted_recoil)

                    PressAndReleaseKey("F8")
                    if not IsMouseButtonPressed(1) then
                        break
                    end
                    break
                end
            end

            Sleep(1)

        end
    else
        while IsMouseButtonPressed(1) do
            if _config.shooting_state == "stop" then    -- 停止射击
                break
            end

            local current_click_time = GetRunningTime() -- 当前点击时间
            bullet_count = math.ceil((current_click_time - start_shooting_time) / _intervals)  -- 子弹数

            for _,recoil_data in ipairs(_config.recoil) do
                if recoil_data[1] == bullet_count then
                    total_coefficient = calculate_influencing_factor()
                    local adjusted_recoil = ceil_and_cache(recoil_data[2] * total_coefficient)
                    MoveMouseRelative(0, adjusted_recoil)

                    if not IsMouseButtonPressed(1) then
                        break
                    end
                    break
                end
            end

            Sleep(1)

        end
    end
end


function event_handing(event, key)
    if event == "mouse_button_down" then
        if key == 1 then
            start_shooting_time = GetRunningTime()
            pressure_grab()
        elseif key == 2 then
            OutputLogMessage("Right button pressed\n")
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

function g1_down() g1___ = true event_handing("mouse_button_down",1,"mouse") end
function g1_up() g1___ = false event_handing("mouse_button_up",1,"mouse") end
function g2_down() g2___ = true event_handing("mouse_button_down",2,"mouse") end
function g2_up() g2___ = false event_handing("mouse_button_up",2,"mouse") end
function g3_down() g3___ = true event_handing("mouse_button_down",3,"mouse") end
function g3_up() g3___ = false event_handing("mouse_button_up",3,"mouse") end
function g4_down() g4___ = true event_handing("mouse_button_down",4,"mouse") end
function g4_up() g4___ = false event_handing("mouse_button_up",4,"mouse") end
function g5_down() g5___ = true event_handing("mouse_button_down",5,"mouse") end
function g5_up() g5___ = false event_handing("mouse_button_up",5,"mouse") end


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
  Sleep(1)
end