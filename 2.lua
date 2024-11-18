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
        default = {
            { 1, 18 },
            { 2, 29 },
            { 3, 17 },
            { 4, 39 },
            { 5, 21 },
            { 6, 41 },
            { 7, 21 },
            { 8, 45 },
            { 9, 25 },
            { 10, 49 },
            { 11, 25 },
            { 12, 49 },
            { 13, 25 },
            { 14, 49 },
            { 15, 29 },
            { 16, 57 },
            { 17, 30 },
            { 18, 59 },
            { 19, 30 },
            { 20, 59 },
            { 21, 30 },
            { 22, 59 },
            { 23, 30 },
            { 24, 59 },
            { 25, 30 },
            { 26, 59 },
            { 27, 30 },
            { 28, 59 },
            { 29, 30 },
            { 30, 59 },
            { 31, 30 },
            { 32, 59 },
            { 33, 30 },
            { 34, 59 },
            { 35, 30 },
            { 36, 59 },
            { 37, 30 },
            { 38, 59 },
            { 39, 30 },
            { 40, 59 },
            { 41, 30 }
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
            { 1, 24 },
            { 2, 17 },
            { 3, 9 },
            { 4, 25 },
            { 5, 16 },
            { 6, 35 },
            { 7, 20 },
            { 8, 39 },
            { 9, 20 },
            { 10, 41 },
            { 11, 23 },
            { 12, 49 },
            { 13, 25 },
            { 14, 49 },
            { 15, 26 },
            { 16, 51 },
            { 17, 27 },
            { 18, 53 },
            { 19, 27 },
            { 20, 53 },
            { 21, 27 },
            { 22, 53 },
            { 23, 27 },
            { 24, 53 },
            { 25, 27 },
            { 26, 53 },
            { 27, 27 },
            { 28, 53 },
            { 29, 27 },
            { 30, 53 },
            { 31, 27 },
            { 32, 55 },
            { 33, 28 },
            { 34, 55 },
            { 35, 28 },
            { 36, 55 },
            { 37, 28 },
            { 38, 55 },
            { 39, 28 },
            { 40, 55 },
            { 41, 28 }
        },
    },

    AKM = {
        default = {
            { 1, 16 },
            { 2, 25 },
            { 3, 13 },
            { 4, 23 },
            { 5, 16 },
            { 6, 31 },
            { 7, 16 },
            { 8, 35 },
            { 9, 20 },
            { 10, 39 },
            { 11, 21 },
            { 12, 41 },
            { 13, 21 },
            { 14, 41 },
            { 15, 21 },
            { 16, 43 },
            { 17, 22 },
            { 18, 43 },
            { 19, 22 },
            { 20, 43 },
            { 21, 22 },
            { 22, 43 },
            { 23, 22 },
            { 24, 43 },
            { 25, 22 },
            { 26, 43 },
            { 27, 22 },
            { 28, 43 },
            { 29, 22 },
            { 30, 43 },
            { 31, 22 },
            { 32, 43 },
            { 33, 22 },
            { 34, 43 },
            { 35, 22 },
            { 36, 43 },
            { 37, 22 },
            { 38, 43 },
            { 39, 22 },
            { 40, 43 },
            { 41, 22 }
        },
    },

    M416 = {
        default = {
            { 1, 23 },
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

    ACE32 = {
        default = {
            { 1, 18 },
            { 2, 23 },
            { 3, 12 },
            { 4, 29 },
            { 5, 17 },
            { 6, 37 },
            { 7, 20 },
            { 8, 39 },
            { 9, 21 },
            { 10, 41 },
            { 11, 21 },
            { 12, 43 },
            { 13, 23 },
            { 14, 45 },
            { 15, 23 },
            { 16, 45 },
            { 17, 23 },
            { 18, 47 },
            { 19, 25 },
            { 20, 51 },
            { 21, 26 },
            { 22, 51 },
            { 23, 26 },
            { 24, 51 },
            { 25, 27 },
            { 26, 53 },
            { 27, 27 },
            { 28, 53 },
            { 29, 27 },
            { 30, 53 },
            { 31, 27 },
            { 32, 53 },
            { 33, 27 },
            { 34, 53 },
            { 35, 27 },
            { 36, 53 },
            { 37, 27 },
            { 38, 53 },
            { 39, 27 },
            { 40, 53 },
            { 41, 27 }
        },
    },

    G36C = {
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
        },
    },

    Scar = {
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
            { 24, 41 },
            { 25, 21 },
            { 26, 41 },
            { 27, 21 },
            { 28, 41 },
            { 29, 21 },
            { 30, 41 },
            { 31, 21 },
            { 32, 41 },
            { 33, 21 },
            { 34, 41 },
            { 35, 21 },
            { 36, 41 },
            { 37, 21 },
            { 38, 41 },
            { 39, 21 },
            { 40, 41 },
            { 41, 21 }
        },
    },

    QBZ = {
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

    K2 = {
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
            { 24, 41 },
            { 25, 21 },
            { 26, 41 },
            { 27, 21 },
            { 28, 41 },
            { 29, 21 },
            { 30, 41 },
            { 31, 21 },
            { 32, 41 },
            { 33, 21 },
            { 34, 41 },
            { 35, 21 },
            { 36, 41 },
            { 37, 21 },
            { 38, 41 },
            { 39, 21 },
            { 40, 41 },
            { 41, 21 }
        },
    },

    M16 = {
        default = {
            { 1, 6 },
            { 2, 11 },
            { 3, 7 },
            { 4, 13 },
            { 5, 8 },
            { 6, 23 },
            { 7, 12 },
            { 8, 23 },
            { 9, 12 },
            { 10, 23 },
            { 11, 12 },
            { 12, 23 },
            { 13, 12 },
            { 14, 23 },
            { 15, 12 },
            { 16, 23 },
            { 17, 12 },
            { 18, 23 },
            { 19, 12 },
            { 20, 23 },
            { 21, 12 },
            { 22, 23 },
            { 23, 12 },
            { 24, 23 },
            { 25, 12 },
            { 26, 23 },
            { 27, 12 },
            { 28, 23 },
            { 29, 23 },
            { 30, 21 },
            { 31, 11 },
            { 32, 21 },
            { 33, 11 },
            { 34, 21 },
            { 35, 23 },
            { 36, 23 },
            { 37, 12 },
            { 38, 23 },
            { 39, 12 },
            { 40, 23 },
            { 41, 12 },
            { 42, 23 }
        },
    },

    MK47 = {
        default = {
            { 1, 6 },
            { 2, 11 },
            { 3, 9 },
            { 4, 17 },
            { 5, 10 },
            { 6, 27 },
            { 7, 14 },
            { 8, 27 },
            { 9, 14 },
            { 10, 27 },
            { 11, 14 },
            { 12, 27 },
            { 13, 14 },
            { 14, 27 },
            { 15, 14 },
            { 16, 27 },
            { 17, 14 },
            { 18, 27 },
            { 19, 14 },
            { 20, 27 },
            { 21, 14 },
            { 22, 27 },
            { 23, 14 },
            { 24, 27 },
            { 25, 14 },
            { 26, 27 },
            { 27, 14 },
            { 28, 27 },
            { 29, 14 },
            { 30, 27 },
            { 31, 14 },
            { 32, 27 }
        },
    },

    GROZA = {
        default = {
            { 1, 16 },
            { 2, 15 },
            { 3, 13 },
            { 4, 27 },
            { 5, 14 },
            { 6, 27 },
            { 7, 14 },
            { 8, 27 },
            { 9, 14 },
            { 10, 29 },
            { 11, 15 },
            { 12, 31 },
            { 13, 16 },
            { 14, 33 },
            { 15, 18 },
            { 16, 39 },
            { 17, 20 },
            { 18, 39 },
            { 19, 20 },
            { 20, 41 },
            { 21, 21 },
            { 22, 41 },
            { 23, 21 },
            { 24, 41 },
            { 25, 21 },
            { 26, 41 },
            { 27, 21 },
            { 28, 41 },
            { 29, 21 },
            { 30, 42 },
            { 31, 21.5 },
            { 32, 42 },
            { 33, 21.5 },
            { 34, 42 },
            { 35, 21.5 },
            { 36, 42 },
            { 37, 21.5 },
            { 38, 42 },
            { 39, 21.5 },
            { 40, 42 },
            { 41, 21.5 }
        },
    },

    FAMAS = {
        default = {
            { 1, 18 },
            { 2, 11 },
            { 3, 9 },
            { 4, 17 },
            { 5, 10 },
            { 6, 27 },
            { 7, 17 },
            { 8, 35 },
            { 9, 19 },
            { 10, 39 },
            { 11, 21 },
            { 12, 41 },
            { 13, 21 },
            { 14, 41 },
            { 15, 22 },
            { 16, 43 },
            { 17, 22 },
            { 18, 43 },
            { 19, 22 },
            { 20, 43 },
            { 21, 23 },
            { 22, 45 },
            { 23, 23 },
            { 24, 45 },
            { 25, 23 },
            { 26, 45 },
            { 27, 23 },
            { 28, 45 },
            { 29, 23 },
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

    PP19 = {
        default = {
            { 1, 7 },
            { 2, 13 },
            { 3, 8 },
            { 4, 17 },
            { 5, 10 },
            { 6, 21 },
            { 7, 12 },
            { 8, 23 },
            { 9, 12 },
            { 10, 23 },
            { 11, 12 },
            { 12, 20 },
            { 13, 10.5 },
            { 14, 20 },
            { 15, 10.5 },
            { 16, 20 },
            { 17, 10.5 },
            { 18, 20 },
            { 19, 10.5 },
            { 20, 20 },
            { 21, 10.5 },
            { 22, 20 },
            { 23, 10.5 },
            { 24, 20 },
            { 25, 10.5 },
            { 26, 20 },
            { 27, 10.5 },
            { 28, 20 },
            { 29, 10.5 },
            { 30, 20 },
            { 31, 10.5 },
            { 32, 20 },
            { 33, 10.5 },
            { 34, 20 },
            { 35, 10.5 },
            { 36, 20 },
            { 37, 10.5 },
            { 38, 20 },
            { 39, 10.5 },
            { 40, 20 },
            { 41, 10.5 },
            { 42, 20 },
            { 43, 10.5 },
            { 44, 20 },
            { 45, 10.5 },
            { 46, 20 },
            { 47, 10.5 },
            { 48, 20 },
            { 49, 10.5 },
            { 50, 20 },
            { 51, 10.5 },
            { 52, 20 },
            { 53, 10.5 }
        },
    },

    TOM = {
        default = {
            { 1, 8 },
            { 2, 15 },
            { 3, 9 },
            { 4, 21 },
            { 5, 12 },
            { 6, 23 },
            { 7, 13 },
            { 8, 25 },
            { 9, 14 },
            { 10, 29 },
            { 11, 16 },
            { 12, 43 },
            { 13, 22 },
            { 14, 43 },
            { 15, 22 },
            { 16, 43 },
            { 17, 22 },
            { 18, 43 },
            { 19, 22 },
            { 20, 43 },
            { 21, 22 },
            { 22, 43 },
            { 23, 22 },
            { 24, 43 },
            { 25, 22 },
            { 26, 43 },
            { 27, 20 },
            { 28, 39 },
            { 29, 20 },
            { 30, 39 },
            { 31, 20 },
            { 32, 39 },
            { 33, 20 },
            { 34, 39 },
            { 35, 20 },
            { 36, 39 },
            { 37, 20 },
            { 38, 39 },
            { 39, 20 },
            { 40, 39 },
            { 41, 20 },
            { 42, 39 },
            { 43, 20 },
            { 44, 39 },
            { 45, 20 },
            { 46, 39 },
            { 47, 20 },
            { 48, 39 },
            { 49, 20 },
            { 50, 39 }
        },
    },

    UMP = {
        default = {
            { 1, 9 },
            { 2, 17 },
            { 3, 10 },
            { 4, 21 },
            { 5, 12 },
            { 6, 25 },
            { 7, 13 },
            { 8, 25 },
            { 9, 14 },
            { 10, 27 },
            { 11, 14 },
            { 12, 28 },
            { 13, 14.5 },
            { 14, 28 },
            { 15, 14.5 },
            { 16, 28 },
            { 17, 14.5 },
            { 18, 28 },
            { 19, 14.5 },
            { 20, 28 },
            { 21, 14.5 },
            { 22, 28 },
            { 23, 14.5 },
            { 24, 28 },
            { 25, 14.5 },
            { 26, 28 },
            { 27, 14.5 },
            { 28, 28 },
            { 29, 14.5 },
            { 30, 28 },
            { 31, 14.5 },
            { 32, 28 },
            { 33, 14.5 },
            { 34, 28 },
            { 35, 14.5 }
        },
    },

    UZI = {
        default = {
            { 1, 7 },
            { 2, 13 },
            { 3, 8 },
            { 4, 15 },
            { 5, 9 },
            { 6, 19 },
            { 7, 11 },
            { 8, 23 },
            { 9, 13 },
            { 10, 27 },
            { 11, 14 },
            { 12, 40 },
            { 13, 20.5 },
            { 14, 40 },
            { 15, 20.5 },
            { 16, 40 },
            { 17, 20.5 },
            { 18, 40 },
            { 19, 20.5 },
            { 20, 44 },
            { 21, 22.5 },
            { 22, 44 },
            { 23, 22.5 },
            { 24, 44 },
            { 25, 22.5 },
            { 26, 44 },
            { 27, 22.5 },
            { 28, 46 },
            { 29, 23.5 },
            { 30, 46 },
            { 31, 23.5 },
            { 32, 46 },
            { 33, 23.5 },
            { 34, 46 },
            { 35, 23.5 }
        },
    },

    VECTOR = {
        default = {
            { 1, 11 },
            { 2, 19 },
            { 3, 11 },
            { 4, 23 },
            { 5, 13 },
            { 6, 27 },
            { 7, 15 },
            { 8, 31 },
            { 9, 17 },
            { 10, 33 },
            { 11, 19 },
            { 12, 40 },
            { 13, 22.5 },
            { 14, 48 },
            { 15, 27.5 },
            { 16, 54 },
            { 17, 27.5 },
            { 18, 54 },
            { 19, 27.5 },
            { 20, 54 },
            { 21, 27.5 },
            { 22, 54 },
            { 23, 27.5 },
            { 24, 54 },
            { 25, 27.5 },
            { 26, 54 },
            { 27, 27.5 },
            { 28, 54 },
            { 29, 27.5 },
            { 30, 54 },
            { 31, 27.5 },
            { 32, 54 },
            { 33, 27.5 }
        },
    },

    MP5 = {
        default = {
            { 1, 16 },
            { 2, 17 },
            { 3, 9 },
            { 4, 23 },
            { 5, 14 },
            { 6, 29 },
            { 7, 16 },
            { 8, 33 },
            { 9, 18 },
            { 10, 37 },
            { 11, 19 },
            { 12, 37 },
            { 13, 19 },
            { 14, 38 },
            { 15, 19.5 },
            { 16, 38 },
            { 17, 19.5 },
            { 18, 38 },
            { 19, 19.5 },
            { 20, 38 },
            { 21, 19.5 },
            { 22, 38 },
            { 23, 19.5 },
            { 24, 38 },
            { 25, 19.5 },
            { 26, 38 },
            { 27, 19.5 },
            { 28, 38 },
            { 29, 19.5 },
            { 30, 38 },
            { 31, 20 },
            { 32, 39 },
            { 33, 20 },
            { 34, 39 },
            { 35, 20 },
            { 36, 39 },
            { 37, 20 },
            { 38, 39 },
            { 39, 20 },
            { 40, 39 }
        },
    },

    P90 = {
        default = {
            { 1, 8 },
            { 2, 15 },
            { 3, 9 },
            { 4, 21 },
            { 5, 12 },
            { 6, 23 },
            { 7, 13 },
            { 8, 25 },
            { 9, 13 },
            { 10, 23 },
            { 11, 14 },
            { 12, 27 },
            { 13, 15 },
            { 14, 29 },
            { 15, 12 },
            { 16, 17.2 },
            { 17, 9.1 },
            { 18, 17.2 },
            { 19, 9.1 },
            { 20, 17.2 },
            { 21, 9.1 },
            { 22, 17.2 },
            { 23, 9.1 },
            { 24, 17.2 },
            { 25, 9.1 },
            { 26, 17.2 },
            { 27, 9.1 },
            { 28, 17.2 },
            { 29, 9.1 },
            { 30, 17.2 },
            { 31, 9.1 },
            { 32, 17.2 },
            { 33, 9.1 },
            { 34, 17.2 },
            { 35, 9.1 },
            { 36, 17.2 },
            { 37, 9.1 },
            { 38, 17.2 },
            { 39, 9.1 },
            { 40, 17.2 },
            { 41, 9.1 },
            { 42, 17.2 },
            { 43, 9.1 },
            { 44, 17.2 },
            { 45, 9.1 },
            { 46, 17.2 },
            { 47, 9.1 },
            { 48, 17.2 },
            { 49, 9.1 },
            { 50, 17.2 }
        },
    },

    JS9 = {
        default = {
            { 1, 10 },
            { 2, 13 },
            { 3, 7 },
            { 4, 19 },
            { 5, 12 },
            { 6, 25 },
            { 7, 13 },
            { 8, 25 },
            { 9, 13 },
            { 10, 25 },
            { 11, 13 },
            { 12, 25 },
            { 13, 15 },
            { 14, 36 },
            { 15, 18.5 },
            { 16, 36 },
            { 17, 18.5 },
            { 18, 36 },
            { 19, 18.5 },
            { 20, 36 },
            { 21, 18.5 },
            { 22, 36 },
            { 23, 18.5 },
            { 24, 36 },
            { 25, 18.5 },
            { 26, 36 },
            { 27, 18.5 },
            { 28, 36 },
            { 29, 18.5 },
            { 30, 36 },
            { 31, 18.5 },
            { 32, 36 },
            { 33, 18.5 },
            { 34, 36 },
            { 35, 18.5 },
            { 36, 36 },
            { 37, 18.5 },
            { 38, 36 },
            { 39, 18.5 },
            { 40, 36 }
        },
    },

    MP9 = {
        default = {
            { 1, 7 },
            { 2, 13 },
            { 3, 8 },
            { 4, 15 },
            { 5, 9 },
            { 6, 19 },
            { 7, 11 },
            { 8, 23 },
            { 9, 12 },
            { 10, 23 },
            { 11, 12 },
            { 12, 24 },
            { 13, 12.5 },
            { 14, 24 },
            { 15, 12.5 },
            { 16, 24 },
            { 17, 12.5 },
            { 18, 22 },
            { 19, 8.5 },
            { 20, 16 },
            { 21, 7.5 },
            { 22, 14 },
            { 23, 7.5 },
            { 24, 14 },
            { 25, 7.5 },
            { 26, 14 },
            { 27, 7.5 },
            { 28, 14 },
            { 29, 7.5 },
            { 30, 14 },
            { 31, 7.5 },
            { 32, 14 },
            { 33, 7.5 },
            { 34, 14 },
            { 35, 7.5 }
        },
    },

    M249 = {
        default = {
            { 1, 15 },
            { 2, 9 },
            { 3, 4 },
            { 4, 15 },
            { 5, 9 },
            { 6, 19 },
            { 7, 10 },
            { 8, 23 },
            { 9, 12 },
            { 10, 19 },
            { 11, 10 },
            { 12, 19 },
            { 13, 8 },
            { 14, 13 },
            { 15, 8 },
            { 16, 15 },
            { 17, 7 },
            { 18, 13 },
            { 19, 7 },
            { 20, 13 },
            { 21, 7 },
            { 22, 13 },
            { 23, 7 },
            { 24, 13 },
            { 25, 7 },
            { 26, 13 },
            { 27, 7 },
            { 28, 13 },
            { 29, 7 },
            { 30, 13 },
            { 31, 7 },
            { 32, 13 },
            { 33, 7 },
            { 34, 13 },
            { 35, 7 },
            { 36, 13 },
            { 37, 7 },
            { 38, 13 },
            { 39, 7 },
            { 40, 13 },
            { 41, 7 },
            { 42, 13 },
            { 43, 7 },
            { 44, 13 },
            { 45, 7 },
            { 46, 13 },
            { 47, 7 },
            { 48, 13 },
            { 49, 7 },
            { 50, 13 },
            { 51, 7 },
            { 52, 13 },
            { 53, 7 },
            { 54, 13 },
            { 55, 7 },
            { 56, 13 },
            { 57, 7 },
            { 58, 13 },
            { 59, 7 },
            { 60, 13 },
            { 61, 7 },
            { 62, 13 },
            { 63, 7 },
            { 64, 13 },
            { 65, 7 },
            { 66, 13 },
            { 67, 7 },
            { 68, 13 },
            { 69, 7 },
            { 70, 13 },
            { 71, 7 },
            { 72, 13 },
            { 73, 7 },
            { 74, 13 },
            { 75, 7 },
            { 76, 13 },
            { 77, 7 },
            { 78, 13 },
            { 79, 7 },
            { 80, 13 },
            { 81, 7 },
            { 82, 13 },
            { 83, 7 },
            { 84, 13 },
            { 85, 7 },
            { 86, 13 },
            { 87, 7 },
            { 88, 13 },
            { 89, 7 },
            { 90, 13 },
            { 91, 7 },
            { 92, 13 },
            { 93, 7 },
            { 94, 13 },
            { 95, 7 },
            { 96, 13 },
            { 97, 7 },
            { 98, 13 },
            { 99, 7 },
            { 100, 13 },
            { 101, 7 },
            { 102, 13 },
            { 103, 7 },
            { 104, 13 },
            { 105, 7 },
            { 106, 13 },
            { 107, 7 },
            { 108, 13 },
            { 109, 7 },
            { 110, 13 },
            { 111, 7 },
            { 112, 13 },
            { 113, 7 },
            { 114, 13 },
            { 115, 7 },
            { 116, 13 },
            { 117, 7 },
            { 118, 13 },
            { 119, 7 },
            { 120, 13 },
            { 121, 7 },
            { 122, 13 },
            { 123, 7 },
            { 124, 13 },
            { 125, 7 },
            { 126, 13 },
            { 127, 7 },
            { 128, 13 },
            { 129, 7 },
            { 130, 13 },
            { 131, 7 },
            { 132, 13 },
            { 133, 7 },
            { 134, 13 },
            { 135, 7 },
            { 136, 13 },
            { 137, 7 },
            { 138, 13 },
            { 139, 7 },
            { 140, 13 },
            { 141, 7 },
            { 142, 13 },
            { 143, 7 },
            { 144, 13 },
            { 145, 7 },
            { 146, 13 },
            { 147, 7 },
            { 148, 13 },
            { 149, 7 },
            { 150, 13 },
            { 151, 7 },
            { 152, 13 },
            { 153, 7 },
            { 154, 13 },
            { 155, 7 },
            { 156, 13 },
            { 157, 7 },
            { 158, 13 },
            { 159, 7 },
            { 160, 13 },
            { 161, 7 },
            { 162, 13 },
            { 163, 7 },
            { 164, 13 },
            { 165, 7 },
            { 166, 13 },
            { 167, 7 },
            { 168, 13 },
            { 169, 7 },
            { 170, 13 }

        },
    },
    MG3 = {
        default = {
            { 1, 11 },
            { 2, 1 },
            { 3, 1 },
            { 4, 5 },
            { 5, 3 },
            { 6, 5 },
            { 7, 3 },
            { 8, 5 },
            { 9, 3 },
            { 10, 5 },
            { 11, 2 },
            { 12, 3 },
            { 13, 2 },
            { 14, 3 },
            { 15, 1 },
            { 16, 3 },
            { 17, 2 },
            { 18, 3 },
            { 19, 2 },
            { 20, 3 },
            { 21, 2 },
            { 22, 3 },
            { 23, 2 },
            { 24, 3 },
            { 25, 2 },
            { 26, 1 },
            { 27, 1 },
            { 28, 1 },
            { 29, 1 },
            { 30, 1 },
            { 31, 1 },
            { 32, 1 },
            { 33, 1 },
            { 34, 1 },
            { 35, 3 },
            { 36, 3 },
            { 37, 2 },
            { 38, 3 },
            { 39, 2 },
            { 40, 3 },
            { 41, 2 },
            { 42, 3 },
            { 43, 2 },
            { 44, 3 },
            { 45, 2 },
            { 46, 3 },
            { 47, 2 },
            { 48, 3 },
            { 49, 2 },
            { 50, 3 },
            { 51, 2 },
            { 52, 3 },
            { 53, 2 },
            { 54, 3 },
            { 55, 2 },
            { 56, 3 },
            { 57, 2 },
            { 58, 3 },
            { 59, 2 },
            { 60, 3 },
            { 61, 2 },
            { 62, 3 },
            { 63, 2 },
            { 64, 3 },
            { 65, 2 },
            { 66, 3 },
            { 67, 2 },
            { 68, 3 },
            { 69, 2 },
            { 70, 3 },
            { 71, 2 },
            { 72, 3 },
            { 73, 2 },
            { 74, 3 },
            { 75, 2 }
        },
    },


    MINI = {
        default = {
            { 1, 6 },
            { 2, 11 },
            { 3, 6 },
            { 4, 11 },
            { 5, 6 },
            { 6, 11 },
            { 7, 6 },
            { 8, 11 },
            { 9, 6 },
            { 10, 11 },
            { 11, 6 },
            { 12, 11 },
            { 13, 6 },
            { 14, 11 },
            { 15, 6 },
            { 16, 11 },
            { 17, 6 },
            { 18, 11 },
            { 19, 6 },
            { 20, 11 },
            { 21, 6 },
            { 22, 11 },
            { 23, 6 },
            { 24, 11 },
            { 25, 6 },
            { 26, 11 },
            { 27, 6 },
            { 28, 11 },
            { 29, 6 },
            { 30, 11 }

        },
        burst = {

            { 1, 10 },
            { 2, 12 },
            { 3, 12 },
            { 4, 32 },
            { 5, 15 },
            { 6, 31 },
            { 7, 15 },
            { 8, 31 },
            { 9, 15 },
            { 10, 31 },
            { 11, 15 },
            { 12, 31 },
            { 13, 15 },
            { 14, 31 },
            { 15, 16 },
            { 16, 31 },
            { 17, 16 },
            { 18, 31 },
            { 19, 16 },
            { 20, 31 },
            { 21, 16 },
            { 22, 31 },
            { 23, 16 },
            { 24, 31 },
            { 25, 16 },
            { 26, 31 },
            { 27, 16 },
            { 28, 31 },
            { 29, 16 },
            { 30, 31 },
            { 31, 16 },
            { 32, 31 },
        },
    },
    SLR = {
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

            { 1, 18 },
            { 2, 18 },
            { 3, 21 },
            { 4, 26 },
            { 5, 22 },
            { 6, 32 },
            { 7, 25 },
            { 8, 32 },
            { 9, 25 },
            { 10, 32 },
            { 11, 24 },
            { 12, 30 },
            { 13, 24 },
            { 14, 30 },
            { 15, 24 },
            { 16, 30 },
            { 17, 20 },
            { 18, 30 },
            { 19, 20 },
            { 20, 30 },
            { 21, 20 },
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
    SKS = {
        default = {
            { 1, 4 },
            { 2, 7 },
            { 3, 4 },
            { 4, 7 },
            { 5, 4 },
            { 6, 7 },
            { 7, 4 },
            { 8, 7 },
            { 9, 4 },
            { 10, 7 },
            { 11, 4 },
            { 12, 7 },
            { 13, 4 },
            { 14, 7 },
            { 15, 4 },
            { 16, 7 },
            { 17, 4 },
            { 18, 7 },
            { 19, 4 },
            { 20, 7 }
        },

        burst = {
            { 1, 14 },
            { 2, 21 },
            { 3, 17 },
            { 4, 33 },
            { 5, 22 },
            { 6, 49 },
            { 7, 25 },
            { 8, 49 },
            { 9, 24 },
            { 10, 47 },
            { 11, 28 },
            { 12, 55 },
            { 13, 28 },
            { 14, 55 },
            { 15, 28 },
            { 16, 55 },
            { 17, 28 },
            { 18, 55 },
            { 19, 26 },
            { 20, 53 },
            { 21, 26 },
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
        default = {
            { 1, 6 },
            { 2, 11 },
            { 3, 6 },
            { 4, 11 },
            { 5, 6 },
            { 6, 11 },
            { 7, 6 },
            { 8, 11 },
            { 9, 6 },
            { 10, 11 },
            { 11, 6 },
            { 12, 11 },
            { 13, 6 },
            { 14, 11 },
            { 15, 6 },
            { 16, 11 },
            { 17, 6 },
            { 18, 11 },
            { 19, 6 },
            { 20, 11 }
        },
        burst = {

            { 1, 11 },
            { 2, 9 },
            { 3, 15 },
            { 4, 29 },
            { 5, 17 },
            { 6, 35 },
            { 7, 17 },
            { 8, 35 },
            { 9, 17 },
            { 10, 35 },
            { 11, 17 },
            { 12, 35 },
            { 13, 17 },
            { 14, 35 },
            { 15, 17 },
            { 16, 35 },
            { 17, 17 },
            { 18, 35 },
            { 19, 17 },
            { 20, 35 },
            { 21, 17 },
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
            { 20, 9 },
            { 21, 5 },
            { 22, 9 },
            { 23, 5 },
            { 24, 9 },
            { 25, 5 },
            { 26, 9 },
            { 27, 5 },
            { 28, 9 },
            { 29, 5 },
            { 30, 9 }
        },
        burst = {

            { 1, 10 },
            { 2, 12 },
            { 3, 13 },
            { 4, 31 },
            { 5, 16 },
            { 6, 33 },
            { 7, 18 },
            { 8, 35 },
            { 9, 18 },
            { 10, 35 },
            { 11, 18 },
            { 12, 35 },
            { 13, 18 },
            { 14, 35 },
            { 15, 18 },
            { 16, 35 },
            { 17, 18 },
            { 18, 35 },
            { 19, 15 },
            { 20, 29 },
            { 21, 15 },
            { 22, 29 },
            { 23, 15 },
            { 24, 29 },
            { 25, 15 },
            { 26, 29 },
            { 27, 15 },
            { 28, 29 },
            { 29, 15 },
            { 30, 29 },
            { 31, 15 },
            { 32, 0 },
        },
    },
    MK14 = {
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

    local pattern_type = IsModifierPressed("lctrl") and "burst" or "default"    -- 按住左Ctrl键切换射击模式
    local pattern = recoil_patterns[weapon_name] and recoil_patterns[weapon_name][pattern_type] or
            recoil_patterns[weapon_name] -- 如果没有找到对应的射击模式，就使用默认的射击模式
    local interval = weapon_intervals[weapon_name]  -- 获取武器的射击间隔

    if not pattern or not interval then
        OutputLogMessage("未找到武器的压枪参数: %s\n", weapon_name)
        return
    end

    local posesMultiplier = attachment_multipliers[weapon_name] and attachment_multipliers[weapon_name].poses   --获取姿势的倍率, 用于计算不同姿势的压枪倍率
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

        while IsMouseButtonPressed(1) do
            if shoot == "None" then
                break
            end

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

        while IsMouseButtonPressed(1) do
            if shoot == "None" then
                break
            end
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
local last_shoot = nil

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
    -- 计算压枪倍率, weapon_name: 武器名, muzzles: 枪口, grips: 握把, scopes: 瞄准镜, stocks: 枪托, poses: 姿势, scope_zoom: 瞄准倍率
    local multiplier = global_recoil_multiplier -- 全局倍率
    local weaponData = attachment_multipliers[weapon_name]  -- 武器配件数据
    multiplier = multiplier * (base_coefficients[weapon_name] or 1) -- 基础倍率
    if weaponData then
        -- 如果有武器配件数据
        local posesMultiplier = weaponData.poses    -- 姿势倍率
        local poseKey = IsModifierPressed("lctrl") and (poses == "stand" and "standBurst" or poses == "down" and
                "downBurst" or posesor) or poses   -- 姿势键, 如果按下ctrl键, 则姿势键为standBurst或downBurst, 否则为poses
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
        -- 如果按下shift键,且武器在受呼吸影响的武器列表中, 则乘以呼吸倍率
        multiplier = multiplier * global_breath_multiplier
    end
    multiplier = multiplier * global_sensitivity_multiplier
    multiplier = multiplier * global_vertical_sensitivity_multiplier
    return multiplier
end

function table.contains(table, element)
    -- 判断table中是否包含element
    for _, value in pairs(table) do
        -- 遍历table
        if value == element then
            -- 如果table中的值等于element
            return true
        end
    end
    return false
end

function is_authorized()
    -- 判断是否授权
    local success, chunk = pcall(dofile, addr)  -- 调用dofile函数, 读取addr文件
    if not success then
        OutputLogMessage("Error loading weapon.lua: %s\n", chunk)
        return false
    end
    return type(muzzle) == "string" and muzzle == "None"
end

for weapon_name, patterns in pairs(recoil_patterns) do
    -- 遍历压枪参数, weapon_name: 武器名, patterns: 压枪参数
    for pattern_type, pattern in pairs(patterns) do
        -- 遍历压枪参数类型, pattern_type: 压枪参数类型, pattern: 压枪参数
        for i, data in ipairs(pattern) do
            -- 遍历压枪参数数据, i: 索引, data: 数据
            if i % 2 == 0 then
                -- 如果i是偶数
                pattern[i][2] = (pattern[i][2] + 1) / 2 -- 压枪参数数据的第二个元素加1再除以2
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

