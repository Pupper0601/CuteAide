
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
    dofile(file_address)
end

-- 计算后坐力
function calculate_influencing_factor(scope, muzzle, grip, stock, car, posture_state, in_car, global_lshift,
                                      alone_factor, global_recoil)
    calculation_results = scope * muzzle * grip * stock * posture_state * alone_factor * global_recoil
    if in_car == 1 then     -- 在车上
        calculation_results = calculation_results * car
    end

    if IsModifierPressed("lshift") then     -- 按住左shift
        calculation_results = calculation_results * global_lshift
    end
    return calculation_results
end

start_shooting_time = 0