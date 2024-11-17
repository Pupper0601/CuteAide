EnablePrimaryMouseButtonEvents(true)

addr = "C:/Temp/weapon.lua"

global_recoil_multiplier = 18.4 / 100 --全局系数

global_sensitivity_multiplier = 30 / 75.2--开镜灵敏度，分母+-1范围内调整

global_vertical_sensitivity_multiplier = 121 / 100 --垂直灵敏度比如100的意思就是垂直灵敏度1


global_breath_multiplier = 1  --屏息灵敏度(要自己调）

global_scope_multipliers = { --倍镜灵敏度，分子+-1范围内调整
    None = 1,
    reddot = 1,
    quanxi = 1,
    x2 = 99.1 / 64.52,
    x3 = 104 / 72.41,
    x4 = 103 / 67.21,
    x6 = 109.5 / 75.86,
}

base_coefficients = {
    Berry = 1,
    AUG = 1.0,
    AKM = 1.0,
    M416 = 1.0,
    ACE32 = 1.0,
    G36C = 1.0,
    SCAR = 1.0,
    QBZ = 1.0,
    K2 = 1.0,
    M16 = 1.0,
    MK47 = 1.0,
    GROZA = 1.0,
    FAMAS = 1.0,
    PP19 = 1.0,
    TOM = 1.0,
    UMP = 1.0,
    UZI = 1.0,
    VECTOR = 1.0,
    MP5 = 1.0,
    P90 = 1.0,
    JS9 = 1.0,
    MP9 = 1.0,
    SLR = 1.6,
    MINI = 1.7,
    SKS = 1.05,
    MK12 = 1.7,
    QBU = 1.55,
    DLG = 1.0,
    VSS = 1.0,
    MK14 = 1.8,
    M249 = 1.0,
    MG3 = 1.0,
}

attachment_multipliers = {
    None = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.75,
            crawl = 0.5,
        },
        muzzles = {
            None = 1,
            xy1 = 0.86,
            bc1 = 0.78,
            xx = 1,
            zt = 0.87,
        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.78,
            thumb = 0.83,
        },
        scopes = {
            None = 0.555,
            reddot = 0.555,
            quanxi = 0.555,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },
    Berry = {
        poses = {
            None = 1.02,
            stand = 1.02,
            down = 0.83,
            crawl = 0.58,
        },
        muzzles = {
            None = 1,
            xy1 = 0.85,
            bc1 = 0.79,
            xx = 1,
            zt = 0.87,
        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.82,
            line = 0.78,
            thumb = 0.81,
            light = 0.87,
        },
        scopes = {
            None = 0.555,
            reddot = 0.555,
            quanxi = 0.555,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.444,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    AUG = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.8,
            crawl = 0.5,
        },
        muzzles = {
            None = 1,
            xy1 = 0.84,
            bc1 = 0.78,
            xx = 1,
            zt = 0.86,
        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.84,
            line = 0.78,
            thumb = 0.81,
        },
        scopes = {
            None = 0.555,
            reddot = 0.555,
            quanxi = 0.555,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.444,
        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    AKM = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.75,
            crawl = 0.47,
        },
        muzzles = {
            None = 1,
            xy1 = 0.85,
            bc1 = 0.76,
            xx = 1,
            zt = 0.86,
        },
        grips = {
            None = 1,
        },
        scopes = {
            None = 0.55,
            reddot = 0.55,
            quanxi = 0.55,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.444,
        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    M416 = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.8,
            crawl = 0.5,
        },
        muzzles = {
            None = 1,
            xy1 = 0.86,
            bc1 = 0.79,
            xx = 1,
            zt = 0.88,
        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.8,
            thumb = 0.8,
            light = 0.88,
        },
        scopes = {
            None = 0.555,
            reddot = 0.555,
            quanxi = 0.555,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    ACE32 = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.75,
            crawl = 0.5,
        },
        muzzles = {
            None = 1,
            xy1 = 0.86,
            bc1 = 0.78,
            xx = 1,
            zt = 0.87,
        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.78,
            thumb = 0.8,
            light = 0.86,
        },
        scopes = {
            None = 0.555,
            reddot = 0.555,
            quanxi = 0.555,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    G36C = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.75,
            crawl = 0.5,
        },
        muzzles = {
            None = 1,
            xy1 = 0.86,
            bc1 = 0.78,
            xx = 1,
            zt = 0.87,
        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.79,
            line = 0.78,
            thumb = 0.76,
            light = 0.79,
        },
        scopes = {
            None = 0.55,
            reddot = 0.55,
            quanxi = 0.55,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    SCAR = {
        poses = {
            None = 0.96,
            stand = 0.96,
            down = 0.75,
            crawl = 0.5,
        },
        muzzles = {
            None = 1,
            xy1 = 0.86,
            bc1 = 0.78,
            xx = 1,
            zt = 0.87,
        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.84,
            line = 0.78,
            thumb = 0.8,
            light = 0.82
        },
        scopes = {
            None = 0.5,
            reddot = 0.5,
            quanxi = 0.5,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    QBZ = {
        poses = {
            None = 0.92,
            stand = 0.92,
            down = 0.75,
            crawl = 0.5,
        },
        muzzles = {
            None = 1,
            xy1 = 0.88,
            bc1 = 0.8,
            xx = 1,
            zt = 0.88,
        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.815,
            line = 0.78,
            thumb = 0.83,
            light = 0.79,
        },
        scopes = {
            None = 0.555,
            reddot = 0.555,
            quanxi = 0.555,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    K2 = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.75,
            crawl = 0.5,
        },
        muzzles = {
            None = 1,
            xy1 = 0.86,
            bc1 = 0.78,
            xx = 1,
            zt = 0.87,
        },
        grips = {
            None = 1,
        },
        scopes = {
            None = 0.55,
            reddot = 0.55,
            quanxi = 0.55,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    M16 = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.78,
            crawl = 0.5,
        },
        muzzles = {
            None = 1,
            xy1 = 0.83,
            bc1 = 0.74,
            xx = 1,
            zt = 0.84,
        },
        grips = {
            None = 1,
        },
        scopes = {
            None = 1,
            reddot = 1,
            quanxi = 1,
            x2 = 1.8,
            x3 = 2.6,
            x4 = 3.6,
            x6 = 2.6,

        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    MK47 = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.78,
            crawl = 0.53,
        },
        muzzles = {
            None = 1,
            xy1 = 0.84,
            bc1 = 0.75,
            xx = 1,
            zt = 0.84,
        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.78,
            thumb = 0.83,
        },
        scopes = {
            None = 1,
            reddot = 1,
            quanxi = 1,
            x2 = 1.8,
            x3 = 2.6,
            x4 = 3.6,
            x6 = 2.6,

        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    GROZA = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.7,
            crawl = 0.47,
        },
        muzzles = {
            None = 1,
            xy1 = 0.86,
            bc1 = 0.78,
            xx = 1,
            zt = 0.87,
        },
        grips = {
            None = 1,
        },
        scopes = {
            None = 0.555,
            reddot = 0.555,
            quanxi = 0.555,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    FAMAS = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.75,
            crawl = 0.5,
        },
        muzzles = {
            None = 1,
            xy1 = 0.86,
            bc1 = 0.8,
            xx = 1,
            zt = 0.83,
        },
        grips = {
            None = 1,
        },
        scopes = {
            None = 0.555,
            reddot = 0.555,
            quanxi = 0.555,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    PP19 = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.77,
            crawl = 0.7,
        },
        muzzles = {
            None = 1,
            bc3 = 0.8,
            xy3 = 0.9,
            xx1 = 1,
        },
        grips = {
            None = 1,
            line = 0.78,
        },
        scopes = {
            None = 0.51,
            reddot = 0.51,
            quanxi = 0.51,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    TOM = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.7,
            crawl = 0.62,
        },
        muzzles = {
            None = 1,
            xx1 = 1,
        },
        grips = {
            None = 1,
            line = 0.78,
        },
        scopes = {
            None = 0.51,
            reddot = 0.51,
            quanxi = 0.51,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    UMP = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.74,
            crawl = 0.7,
        },
        muzzles = {
            None = 1,
            bc3 = 0.8,
            xy3 = 0.9,
            xx1 = 1,
        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.79,
            thumb = 0.83,
        },
        scopes = {
            None = 0.52,
            reddot = 0.52,
            quanxi = 0.52,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    UZI = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.73,
            crawl = 0.6,
        },
        muzzles = {
            None = 1,
            bc3 = 0.68,
            xy3 = 0.88,
            xx1 = 1,
        },
        grips = {
            None = 1,
        },
        scopes = {
            None = 0.51,
            reddot = 0.51,
            quanxi = 0.51,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    VECTOR = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.75,
            crawl = 0.64,
        },
        muzzles = {
            None = 1,
            bc3 = 0.8,
            xy3 = 0.9,
            xx1 = 1,
        },
        grips = {
            None = 1,
            red = 0.83,
            line = 0.79,
        },
        scopes = {
            None = 0.52,
            reddot = 0.52,
            quanxi = 0.52,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
            normal = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    MP5 = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.67,
            crawl = 0.53,
        },
        muzzles = {
            None = 1,
            bc3 = 0.6,
            xy3 = 0.82,
            xx1 = 1,
        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.75,
            thumb = 0.83,
        },
        scopes = {
            None = 0.52,
            reddot = 0.52,
            quanxi = 0.52,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
            normal = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    P90 = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.77,
            crawl = 0.67,
        },
        muzzles = {
            None = 1,
        },
        grips = {
            None = 1,
        },
        scopes = {
            None = 0.52,
            reddot = 0.52,
            quanxi = 0.52,
        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    JS9 = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.73,
            crawl = 0.5,
        },
        muzzles = {
            None = 1,
            bc3 = 0.58,
            xy3 = 0.82,
            xx1 = 1,
        },
        grips = {
            None = 1,
        },
        scopes = {
            None = 0.52,
            reddot = 0.52,
            quanxi = 0.52,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    MP9 = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.73,
            crawl = 0.63,
        },
        muzzles = {
            None = 1,
        },
        grips = {
            None = 1,
        },
        scopes = {
            None = 0.52,
            reddot = 0.52,
            quanxi = 0.52,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },
    SLR = {
        poses = {
            None = 1,
            stand = 1.02,
            down = 0.77,
            standBurst = 1.18,
            downBurst = 0.8
        },
        muzzles = {
            None = 1,
            xy1 = 0.94,
            xy2 = 0.94,
            bc1 = 0.9,
            bc2 = 0.9,
            xx = 1,
            zt = 0.88,

        },
        scopes = {
            None = 2.5,
            reddot = 2.5,
            quanxi = 2.5,
            x2 = 1,
            x3 = 1,
            x4 = 1,
            x6 = 0.9,
            x8 = 1,

        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.79,
            thumb = 0.83,
        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },

    },
    MINI = {
        poses = {
            None = 1.05,
            stand = 1.05,
            down = 0.72,
            standBurst = 1.5,
            downBurst = 1
        },
        muzzles = {
            None = 1,
            xy1 = 0.94,
            xy2 = 0.94,
            bc1 = 0.9,
            bc2 = 0.9,
            xx = 1,
            zt = 0.89,

        },
        scopes = {
            None = 1.5,
            reddot = 1.5,
            quanxi = 1.5,
            x2 = 1,
            x3 = 1,
            x4 = 1.1,
            x6 = 1,
            x8 = 1.1,

        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.79,
            thumb = 0.83,
        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },

    },
    SKS = {
        poses = {
            None = 1,
            stand = 1.099,
            down = 2,
            standBurst = 1.5,
            downBurst = 1
        },
        muzzles = {
            None = 1,
            xy1 = 0.94,
            xy2 = 0.94,
            bc1 = 0.9,
            bc2 = 0.9,
            xx = 1,
            zt = 0.87,

        },
        scopes = {
            None = 2.5,
            reddot = 2.5,
            quanxi = 2.5,
            x2 = 1,
            x3 = 1,
            x4 = 0.6,
            x6 = 1,
            x8 = 0.6,

        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.79,
            thumb = 0.83,
        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },

    },
    MK12 = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.78,
            standBurst = 1.43,
            downBurst = 1
        },

        muzzles = {
            None = 1,
            xy1 = 0.94,
            xy2 = 0.94,
            bc1 = 0.9,
            bc2 = 0.9,
            xx = 1,
            zt = 0.85,

        },
        scopes = {
            None = 1.5,
            reddot = 1.5,
            quanxi = 1.5,
            x2 = 1,
            x3 = 1,
            x4 = 1.08,
            x6 = 1,
            x8 = 1.08,

        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.79,
            thumb = 0.83,
        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },

    },
    QBU = {
        poses = {
            None = 1,
            stand = 1,
            down = 0.78,
            standBurst = 1.43,
            downBurst = 1
        },
        muzzles = {
            None = 1,
            xy1 = 0.94,
            xy2 = 0.94,
            bc1 = 0.9,
            bc2 = 0.9,
            xx = 1,
            zt = 0.85,

        },
        scopes = {
            None = 1.5,
            reddot = 1.5,
            quanxi = 1.5,
            x2 = 1,
            x3 = 1,
            x4 = 1,
            x6 = 1,
            x8 = 1,

        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.79,
            thumb = 0.83,
        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },

    },
    DLG = {
        poses = {
            None = 1.3,
            stand = 1.3,
            down = 0.84,

        },
        muzzles = {
            None = 1,
            xy1 = 0.94,
            xy2 = 0.94,
            bc1 = 0.9,
            bc2 = 0.9,
            xx = 1,
            zt = 0.85,

        },
        scopes = {
            None = 2.5,
            reddot = 2.5,
            quanxi = 2.5,
            x2 = 1,
            x3 = 1.8,
            x4 = 1.5,
            x6 = 1.8,
            x8 = 1.5,

        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.79,
            thumb = 0.83,
        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },

    },
    VSS = {
        poses = {
            None = 1,
            stand = 1,
            down = 1,
        },
        muzzles = {
            None = 1,
            xy1 = 1,
            xy2 = 1,
            bc1 = 1,
            bc2 = 1,
            xx = 1,
            zt = 1,

        },
        scopes = {
            None = 1,
            reddot = 1,
            quanxi = 1,
            x2 = 1,
            x3 = 1,
            x4 = 1,
            x6 = 1,
            x8 = 1,

        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.79,
            thumb = 0.83,
        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },

    },
    MK14 = {
        poses = {
            None = 1,
            stand = 0.95,
            down = 0.77,
            standBurst = 1,
            downBurst = 1
        },
        muzzles = {
            None = 1,
            xy1 = 0.94,
            xy2 = 0.94,
            bc1 = 0.9,
            bc2 = 0.9,
            xx = 1,
            zt = 0.85,

        },
        scopes = {
            None = 1,
            reddot = 1,
            quanxi = 1,
            x2 = 1,
            x3 = 1,
            x4 = 1.1,
            x6 = 1,
            x8 = 1.2,

        },
        grips = {
            None = 1,
            angle = 1,
            red = 0.83,
            line = 0.79,
            thumb = 0.83,
        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 0.86,
        },
        car = {
            None = 1,
            car = 1.5,
        },

    },
    M249 = {
        poses = {
            None = 1.28,
            stand = 1.28,
            down = 0.73,
            crawl = 0.3,
        },
        muzzles = {
            None = 1,
        },
        grips = {
            None = 1,
        },
        scopes = {
            None = 0.55,
            reddot = 0.55,
            quanxi = 0.55,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
            normal = 1,
            heavy = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },

    MG3 = {
        poses = {
            None = 3,
            stand = 3,
            down = 1.78,
            crawl = 0.65,
        },
        muzzles = {
            None = 1,
        },
        grips = {
            None = 1,
        },
        scopes = {
            None = 0.52,
            reddot = 0.52,
            quanxi = 0.52,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,

        },
        stocks = {
            None = 1,
        },
        car = {
            None = 1,
            car = 1.5,
        },
    },
}

recoil_patterns = {
    Berry = {
        default = { 18, 29, 17, 39, 21, 41, 21, 45, 25, 49, 25, 49, 25, 49, 29, 57, 30, 59, 30, 59, 30, 59, 30, 59, 30, 59, 30, 59, 30, 59, 30, 59, 30, 59, 30, 59, 30, 59, 30, 59, 30
        },
    },
    None = {
        default = {
            { 1, 16 },
            { 2, 13 },
            { 3, 11 },
            { 4, 23 },
            { 5, 14 },
            { 6, 33 },
            { 7, 17 },
            { 8, 33 },
            { 9, 18 },
            { 10, 37 },
            { 11, 19 },
            { 12, 37 },
            { 13, 19 },
            { 14, 37 },
            { 15, 21 },
            { 16, 41 },
            { 17, 21 },
            { 18, 41 },
            { 19, 21 },
            { 20, 41 },
            { 21, 21 },
            { 22, 41 },
            { 23, 21 },
            { 24, 43 },
            { 25, 22 },
            { 26, 43 },
            { 27, 22 },
            { 28, 43 },
            { 29, 22 },
            { 30, 45 },
            { 31, 23 },
            { 32, 45 },
            { 33, 23 },
            { 34, 45 },
            { 35, 23 },
            { 36, 45 },
            { 37, 23 },
            { 38, 45 },
            { 39, 23 },
            { 40, 45 },
            { 41, 23 }
        },
    },


    AUG = {
        default = {
            24,
            17,
            9,
            25,
            16,
            35,
            20,
            39,
            20,
            41,
            23,
            49,
            25,
            49,
            26,
            51,
            27,
            53,
            27,
            53,
            27,
            53,
            27,
            53,
            27,
            53,
            27,
            53,
            27,
            53,
            27,
            55,
            28,
            55,
            28,
            55,
            28,
            55,
            28,
            55,
            28
        },
    },

    AKM = {
        default = { 16, 25, 13, 23, 16, 31, 16, 35, 20, 39, 21, 41, 21, 41, 21, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22
        },
    },

    M416 = {
        default = { 23, 13, 11, 23, 14, 33, 17, 33, 18, 37, 19, 37, 19, 37, 21, 41, 21, 41, 21, 41, 21, 41, 21, 43, 22, 43, 22, 43, 22, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23
        },
    },

    ACE32 = {
        default = { 18, 23, 12, 29, 17, 37, 20, 39, 21, 41, 21, 43, 23, 45, 23, 45, 23, 47, 25, 51, 26, 51, 26, 51, 27, 53, 27, 53, 27, 53, 27, 53, 27, 53, 27, 53, 27, 53, 27, 53, 27
        },
    },

    G36C = {
        default = { 16, 13, 11, 23, 14, 33, 17, 33, 18, 37, 19, 37, 19, 37, 21, 41, 21, 41, 21, 41, 21, 41, 21, 43, 22, 43, 22, 43, 22, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45,
        },
    },

    Scar = {
        default = { 16, 13, 11, 23, 14, 33, 17, 33, 18, 37, 19, 37, 19, 37, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21
        },
    },

    QBZ = {
        default = { 16, 13, 11, 23, 14, 33, 17, 33, 18, 37, 19, 37, 19, 37, 21, 41, 21, 41, 21, 41, 21, 41, 21, 43, 22, 43, 22, 43, 22, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23
        },
    },

    K2 = {
        default = { 16, 13, 11, 23, 14, 33, 17, 33, 18, 37, 19, 37, 19, 37, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21
        },
    },

    M16 = {
        default = { 6, 11, 7, 13, 8, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 23, 21, 11, 21, 11, 21, 23, 23, 12, 23, 12, 23, 12, 23
        },
    },

    MK47 = {
        default = { 6, 11, 9, 17, 10, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27
        },
    },

    GROZA = {
        default = { 16, 15, 13, 27, 14, 27, 14, 27, 14, 29, 15, 31, 16, 33, 18, 39, 20, 39, 20, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 42, 21.5, 42, 21.5, 42, 21.5, 42, 21.5, 42, 21.5, 42, 21.5
        },
    },

    FAMAS = {
        default = { 18, 11, 9, 17, 10, 27, 17, 35, 19, 39, 21, 41, 21, 41, 22, 43, 22, 43, 22, 43, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23
        },
    },

    PP19 = {
        default = { 7, 13, 8, 17, 10, 21, 12, 23, 12, 23, 12, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5, 20, 10.5
        },
    },

    TOM = {
        default = { 8, 15, 9, 21, 12, 23, 13, 25, 14, 29, 16, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 20, 39, 20, 39, 20, 39, 20, 39, 20, 39, 20, 39, 20, 39, 20, 39, 20, 39, 20, 39, 20, 39, 20, 39
        },
    },

    UMP = {
        default = { 9, 17, 10, 21, 12, 25, 13, 25, 14, 27, 14, 28, 14.5, 28, 14.5, 28, 14.5, 28, 14.5, 28, 14.5, 28, 14.5, 28, 14.5, 28, 14.5, 28, 14.5, 28 }, 14.5, 28, 14.5, 28, 14.5
    },


    UZI = {
        default = { 7, 13, 8, 15, 9, 19, 11, 23, 13, 27, 14, 40, 20.5, 40, 20.5, 40, 20.5, 40, 20.5, 44, 22.5, 44, 22.5, 44, 22.5, 44, 22.5, 46, 23.5, 46, 23.5, 46, 23.5, 46, 23.5
        },
    },

    VECTOR = {
        default = { 11, 19, 11, 23, 13, 27, 15, 31, 17, 33, 19, 40, 22.5, 48, 27.5, 54, 27.5, 54, 27.5, 54, 27.5, 54, 27.5, 54, 27.5, 54, 27.5, 54, 27.5, 54, 27.5, 54, 27.5
        },
    },

    MP5 = {
        default = { 16, 17, 9, 23, 14, 29, 16, 33, 18, 37, 19, 37, 19, 38, 19.5, 38, 19.5, 38, 19.5, 38, 19.5, 38, 19.5, 38, 19.5, 38, 19.5, 38, 19.5, 38, 20, 39, 20, 39, 20, 39, 20, 39, 20, 39
        },
    },

    P90 = {
        default = { 8, 15, 9, 21, 12, 23, 13, 25, 13, 23, 14, 27, 15, 29, 12, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2, 9.1, 17.2
        },
    },

    JS9 = {
        default = { 10, 13, 7, 19, 12, 25, 13, 25, 13, 25, 13, 25, 15, 36, 18.5, 36, 18.5, 36, 18.5, 36, 18.5, 36, 18.5, 36, 18.5, 36, 18.5, 36, 18.5, 36, 18.5, 36, 18.5, 36, 18.5, 36, 18.5, 36, 18.5, 36
        },
    },

    MP9 = {
        default = { 7, 13, 8, 15, 9, 19, 11, 23, 12, 23, 12, 24, 12.5, 24, 12.5, 24, 12.5, 22, 8.5, 16, 7.5, 14, 7.5, 14, 7.5, 14, 7.5, 14, 7.5, 14, 7.5, 14, 7.5, 14, 7.5
        },
    },

    M249 = {
        default = { 15, 9, 4, 15, 9, 19, 10, 23, 12, 19, 10, 19, 8, 13, 8, 15, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13, 7, 13

        },
    },
    MG3 = {
        default = { 11, 1, 1, 5, 3, 5, 3, 5, 3, 5, 2, 3, 2, 3, 1, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2, 3, 2
        },
    },


    MINI = {
        default = { 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11

        },
        burst = {
            10, 12, 12, 32, 15, 31, 15, 31, 15, 31, 15, 31, 15, 31, 16, 31, 16, 31, 16, 31, 16, 31, 16, 31, 16, 31, 16, 31, 16, 31, 16, 31,
        },
    },
    SLR = {
        default = { 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9
        },
        burst = {
            18, 18, 21, 26, 22, 32, 25, 32, 25, 32, 24, 30, 24, 30, 24, 30, 20, 30, 20, 30, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
        },
    },
    SKS = {
        default = { 4, 7, 4, 7, 4, 7, 4, 7, 4, 7, 4, 7, 4, 7, 4, 7, 4, 7, 4, 7
        },

        burst = { 14, 21, 17, 33, 22, 49, 25, 49, 24, 47, 28, 55, 28, 55, 28, 55, 28, 55, 26, 53, 26,
                  { 22, 0 },
                  { 23, 0 },
                  { 24, 0 },
                  { 25, 0 },
                  { 26, 0 },
                  { 27, 0 },
                  { 28, 0 },
                  { 29, 0 },
                  { 30, 0 },
                  { 31, 0 },
                  { 32, 0 },
        },

        DLG = {

            { 1, 20 },
            { 2, 20 },
            { 3, 20 },
            { 4, 20 },
            { 5, 20 },
            { 6, 20 },
            { 7, 20 },
            { 8, 20 },
            { 9, 20 },
            { 10, 20 },
            { 11, 20 },
            { 12, 20 },
            { 13, 20 },
            { 14, 20 },
            { 15, 20 },
            { 16, 20 },
            { 17, 20 },
            { 18, 20 },
            { 19, 20 },
            { 20, 20 },
        },
    },
    QBU = {
        default = { 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11
        },
        burst = {
            11, 9, 15, 29, 17, 35, 17, 35, 17, 35, 17, 35, 17, 35, 17, 35, 17, 35, 17, 35, 17,
            { 22, 0 },
            { 23, 0 },
            { 24, 0 },
            { 25, 0 },
            { 26, 0 },
            { 27, 0 },
            { 28, 0 },
            { 29, 0 },
            { 30, 0 },
            { 31, 0 },
            { 32, 0 },
        },
    },
    MK12 = {
        default = { 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9
        },
        burst = {
            10, 12, 13, 31, 16, 33, 18, 35, 18, 35, 18, 35, 18, 35, 18, 35, 18, 35, 15, 29, 15, 29, 15, 29, 15, 29, 15, 29, 15, 29, 15, 0,
        },
    },
    MK14 = {
        default = { 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9
        },
        burst = {

            { 1, 20 },
            { 2, 20 },
            { 3, 20 },
            { 4, 20 },
            { 5, 20 },
            { 6, 20 },
            { 7, 20 },
            { 8, 20 },
            { 9, 20 },
            { 10, 20 },
            { 11, 20 },
            { 12, 20 },
            { 13, 20 },
            { 14, 20 },
            { 15, 20 },
            { 16, 20 },
            { 17, 20 },
            { 18, 20 },
            { 19, 20 },
            { 20, 20 },
        },
    },
    VSS = {
        default = {
            { 1, 5 },
            { 2, 9 },
            { 3, 5 },
            { 4, 9 },
            { 5, 5 },
            { 6, 9 },
            { 7, 5 },
            { 8, 9 },
            { 9, 5 },
            { 10, 9 },
            { 11, 5 },
            { 12, 9 },
            { 13, 5 },
            { 14, 9 },
            { 15, 5 },
            { 16, 9 },
            { 17, 5 },
            { 18, 9 },
            { 19, 5 },
            { 20, 9 }
        },
        burst = {

            { 1, 20 },
            { 2, 20 },
            { 3, 20 },
            { 4, 20 },
            { 5, 20 },
            { 6, 20 },
            { 7, 20 },
            { 8, 20 },
            { 9, 20 },
            { 10, 20 },
            { 11, 20 },
            { 12, 20 },
            { 13, 20 },
            { 14, 20 },
            { 15, 20 },
            { 16, 20 },
            { 17, 20 },
            { 18, 20 },
            { 19, 20 },
            { 20, 20 },
        },
    },
    DLG = {
        default = {
            { 1, 9 },
            { 2, 17 },
            { 3, 9 },
            { 4, 17 },
            { 5, 9 },
            { 6, 17 },
            { 7, 9 },
            { 8, 17 },
            { 9, 9 },
            { 10, 17 },
            { 11, 9 },
            { 12, 17 },
            { 13, 9 },
            { 14, 17 },
            { 15, 9 },
            { 16, 17 },
            { 17, 9 },
            { 18, 17 },
            { 19, 9 },
            { 20, 17 }

        },
        burst = {

            { 1, 20 },
            { 2, 20 },
            { 3, 20 },
            { 4, 20 },
            { 5, 20 },
            { 6, 20 },
            { 7, 20 },
            { 8, 20 },
            { 9, 20 },
            { 10, 20 },
            { 11, 20 },
            { 12, 20 },
            { 13, 20 },
            { 14, 20 },
            { 15, 20 },
            { 16, 20 },
            { 17, 20 },
            { 18, 20 },
            { 19, 20 },
            { 20, 20 },
        },
    },

}

local weapon_intervals = {
    None = 86,
    Berry = 86,
    AUG = 84,
    AKM = 102,
    M416 = 87,
    ACE32 = 89,
    G36C = 87,
    Scar = 87,
    QBZ = 87,
    K2 = 87,
    M16 = 78,
    MK47 = 76,
    GROZA = 80,
    FAMAS = 67,
    PP19 = 84,
    TOM = 80,
    UMP = 88,
    UZI = 48,
    VECTOR = 54,
    MP5 = 66,
    P90 = 60,
    JS9 = 66,
    MP9 = 60,
    DP28 = 66,
    M249 = 75,
    MG3 = 61,
    MINI = 108,
    SLR = 108,
    SKS = 108,
    MK12 = 108,
    QBU = 108,
    DLG = 108,
    VSS = 108,
    MK14 = 108,
}

local weapon_intervals = {
    None = 86,
    Berry = 86,
    AUG = 84,
    AKM = 102,
    M416 = 87,
    ACE32 = 89,
    G36C = 87,
    SCAR = 87,
    QBZ = 87,
    K2 = 87,
    M16 = 78,
    MK47 = 76,
    GROZA = 80,
    FAMAS = 67,
    PP19 = 84,
    TOM = 80,
    UMP = 88,
    UZI = 48,
    VECTOR = 54,
    MP5 = 66,
    P90 = 60,
    JS9 = 66,
    MP9 = 60,
    DP28 = 66,
    M249 = 75,
    MG3 = 61,
    MINI = 108,
    SLR = 108,
    SKS = 108,
    MK12 = 108,
    QBU = 108,
    DLG = 108,
    VSS = 108,
    MK14 = 108,
}

local decimal_cache = 0

function ceil_and_cache(value)
    local integer_part = math.floor(value)
    decimal_cache = decimal_cache + value - integer_part
    if decimal_cache >= 1 then
        integer_part = integer_part + 1
        decimal_cache = decimal_cache - 1
    end
    return integer_part
end

local burstModeEnabled = false
local debugModeEnabled = false

local weaponBurstModes = {}

local ClickStartTime = 0

function Sleep2(t)
    local sleepTime = GetRunningTime()
    while GetRunningTime() - sleepTime <= t do
    end
end

function apply_recoil(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, car)
    if not is_authorized() then
        return
    end

    local pattern_type = IsModifierPressed("lctrl") and "burst" or "default"
    local pattern = recoil_patterns[weapon_name] and recoil_patterns[weapon_name][pattern_type] or recoil_patterns[weapon_name]
    local interval = weapon_intervals[weapon_name]

    if not pattern or not interval then
        OutputLogMessage("未找到武器的压枪参数: %s\n", weapon_name)
        return
    end

    local posesMultiplier = attachment_multipliers[weapon_name] and attachment_multipliers[weapon_name].poses
    local standMultiplier = 1
    local downMultiplier = 1

    if posesMultiplier then
        standMultiplier = posesMultiplier[poses] or 1
        downMultiplier = posesMultiplier[poses] or 1

        if pattern_type == "burst" then
            standMultiplier = posesMultiplier["standBurst"] or standMultiplier
            downMultiplier = posesMultiplier["downBurst"] or downMultiplier
        end
    end

    local multiplier = calculate_recoil_multiplier(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, car)
    local bullet_count = 0

    if weapon_name == "MK47" or weapon_name == "M16" or weapon_name == "None" or weapon_name == "MINI" or weapon_name == "SKS" or weapon_name == "MK12" or weapon_name == "SLR" or weapon_name == "QBU" then
        while IsMouseButtonPressed(1) and (IsMouseButtonPressed(3) or IsMouseButtonPressed(4)) do
            local ClickCurrentTime = GetRunningTime()
            bullet_count = math.ceil((ClickCurrentTime - ClickStartTime) / interval)

            for _, recoil_data in ipairs(pattern) do
                if recoil_data[1] == bullet_count then
                    poses = read_poses_file()
                    multiplier = calculate_recoil_multiplier(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, car)
                    local adjusted_recoil = ceil_and_cache(recoil_data[2] * multiplier)
                    MoveMouseRelative(0, adjusted_recoil)
                    PressAndReleaseKey("F8")

                    if debugModeEnabled then
                        MoveMouseRelative(1, 0)
                    end
                    if not IsMouseButtonPressed(1) then
                        break
                    end
                    break
                end

            end
            Sleep2(1)

        end

    else

        while IsMouseButtonPressed(1) and (IsMouseButtonPressed(3) or IsMouseButtonPressed(4)) do
            local ClickCurrentTime = GetRunningTime()
            bullet_count = math.ceil((ClickCurrentTime - ClickStartTime) / interval)

            for _, recoil_data in ipairs(pattern) do
                if recoil_data[1] == bullet_count then
                    poses = read_poses_file()
                    multiplier = calculate_recoil_multiplier(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, car)
                    local adjusted_recoil = ceil_and_cache(recoil_data[2] * multiplier)
                    MoveMouseRelative(0, adjusted_recoil)
                    if not IsMouseButtonPressed(1) then
                        break
                    end
                    if debugModeEnabled then
                        MoveMouseRelative(1, 0)
                    end

                    break
                end
            end

            Sleep2(1)

        end
    end
end

local last_weapon_name = nil
local last_muzzles = nil
local last_grips = nil
local last_scopes = nil
local last_stocks = nil
local last_poses = nil

function read_weapon_from_file()
    if not is_authorized() then
        return nil
    end
    weapon_name = nil
    scopes = nil
    muzzles = nil
    stocks = nil
    poses = nil
    shoot = nil
    car = nil

    dofile(addr)

    if weapon_name then

        last_weapon_name = weapon_name
        last_muzzles = muzzles
        last_grips = grips
        last_scopes = scopes
        last_stocks = stocks
        last_poses = poses
        last_shoot = shoot
        last_car = car

        local output = string.format("%s+%s+%s+%s+%s+%s+%s+%s+%s", weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, shoot, car)
        OutputLogMessage("%s\n", output)
        return weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, shoot, car
    else
        OutputLogMessage("未找到武器信息, 使用上一次的武器信息\n")

        return last_weapon_name, last_muzzles, last_grips, last_scopes, last_stocks, last_poses, last_scope_zoom, last_shoot, last_car
    end
end

function read_poses_file()
    if not is_authorized() then
        return nil
    end
    poses = nil

    dofile(addr)

    if weapon_name then

        last_poses = poses

        return poses
    else
        return last_poses
    end
end

function OnEvent(event, arg)
    if event == "PROFILE_ACTIVATED" then
        EnablePrimaryMouseButtonEvents(true)
    elseif event == "PROFILE_DEACTIVATED" then
        EnablePrimaryMouseButtonEvents(false)
    elseif event == "MOUSE_BUTTON_PRESSED" then
        if arg == 1 then
            ClickStartTime = GetRunningTime()
            PressKey("F8")
            local weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, car = read_weapon_from_file()
            if not scope_zoom then
                scope_zoom = 1
            end
            if weapon_name then
                apply_recoil(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, car)
            end
        elseif arg == 2 then
            local weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, car = read_weapon_from_file()
            if weapon_name then
                local output = string.format("%s+%s+%s+%s+%s+%s+%s+%s", weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, car)
                OutputLogMessage("%s\n", output)
            end
        elseif arg == 5 and IsModifierPressed("lctrl") then

            local weapon_name = read_weapon_from_file()
            if weapon_name then
                weaponBurstModes[weapon_name] = not weaponBurstModes[weapon_name]
                OutputLogMessage("weapon %s tututu %s\n", weapon_name, weaponBurstModes[weapon_name] and "on" or "close")
            end
        elseif arg == 4 and IsModifierPressed("lctrl") then
            debugModeEnabled = not debugModeEnabled
            OutputLogMessage("debug%s\n", debugModeEnabled and "on" or "close")
        elseif arg == 9 then
            fastPickup()
        end
    elseif event == "MOUSE_BUTTON_RELEASED" then
        if arg == 1 then
            ReleaseKey("F8")
            MoveMouseRelative(0, 0)
        end
    end

    if (event == "MOUSE_BUTTON_PRESSED" and arg == pick and IsModifierPressed("lctrl")) then
        autopick()
    end
end

pick = 3
autopick = function()
    PressAndReleaseKey("tab")
    Sleep2(50)
    for k = 1, 5 do
        for j = 1, 5 do
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

function calculate_recoil_multiplier(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom)
    local multiplier = global_recoil_multiplier
    local weaponData = attachment_multipliers[weapon_name]
    multiplier = multiplier * (base_coefficients[weapon_name] or 1)
    if weaponData then
        local posesMultiplier = weaponData.poses
        local poseKey = IsModifierPressed("lctrl") and (poses == "stand" and "standBurst" or poses == "down" and "downBurst" or posesor) or poses
        multiplier = multiplier * (posesMultiplier[poseKey] or 1)
        multiplier = multiplier * (weaponData.muzzles[muzzles] or 1)
        multiplier = multiplier * (weaponData.grips[grips] or 1)
        multiplier = multiplier * (weaponData.scopes[scopes] or 1)
        multiplier = multiplier * (weaponData.stocks[stocks] or 1)
        multiplier = multiplier * (weaponData.car[car] or 1)
        multiplier = multiplier * scope_zoom
    end
    multiplier = multiplier * (global_scope_multipliers[scopes] or 1)
    local breath_affected_weapons = { "Berry", "AUG", "AKM", "M416", "ACE32", "G36C", "SCAR", "QBZ", "K2", "M16", "MK47", "GROZA", "FAMAS", "PP19", "TOM", "UMP", "UZI", "VECTOR", "MP5", "P90", "JS9", "MP9", "M249", "MG3" }
    if IsModifierPressed("lshift") and table.contains(breath_affected_weapons, weapon_name) then
        multiplier = multiplier * global_breath_multiplier
    end
    multiplier = multiplier * global_sensitivity_multiplier
    multiplier = multiplier * global_vertical_sensitivity_multiplier
    return multiplier
end
function table.contains(table, element)
    for _, value in pairs(table) do
        if value == element then
            return true
        end
    end
    return false
end
function is_authorized()
    local success, chunk = pcall(dofile, addr)
    if not success then
        OutputLogMessage("Error loading weapon.lua: %s\n", chunk)
        return false
    end
    return type(muzzle) == "string" and muzzle == "None"
end
for weapon_name, patterns in pairs(recoil_patterns) do
    for pattern_type, pattern in pairs(patterns) do
        for i, data in ipairs(pattern) do
            if i % 2 == 0 then
                pattern[i][2] = (pattern[i][2] + 1) / 2
            end
        end
    end
end
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

