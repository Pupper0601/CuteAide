EnablePrimaryMouseButtonEvents(true)

addr = "C:/Temp/weapon.lua"



global_sensitivity_multiplier = 30/30  --开镜灵敏度，分母+-1范围内调整

global_vertical_sensitivity_multiplier = 121/121 --垂直灵敏度比如100的意思就是垂直灵敏度1


global_breath_multiplier = 1  --屏息灵敏度(要自己调）

global_scope_multipliers = { --倍镜灵敏度，分子+-1范围内调整
    None = 1,
    reddot = 33/33,
    quanxi = 1,
    x2 = 0.6,
    x3 = 42/72.41,
    x4 = 41/67.21,
    x6 = 44/75.86,
    x8 = 44/21.26,
}





local base_coefficients = {
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




local attachment_multipliers = {
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
            none = 0.555,
            none1 = 0.555,
            none2 = 0.555,
            none3 = 0.555,
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
none = 0.555,
            none1 = 0.555,
            none2 = 0.555,
            none3 = 0.555,
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
none = 0.555,
            none1 = 0.555,
            none2 = 0.555,
            none3 = 0.555,
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
none = 0.55,
            none1 = 0.55,
            none2 = 0.55,
            none3 = 0.55,
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
            down = 0.75,
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
            line = 0.78,
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
none = 0.555,
            none1 = 0.555,
            none2 = 0.555,
            none3 = 0.555,
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
            light= 0.86,
        },
        scopes = {
            None = 0.555,
            reddot = 0.555,
            quanxi = 0.555,
            x2 = 1,
            x3 = 1.444,
            x4 = 2,
            x6 = 1.455,
none = 0.555,
            none1 = 0.555,
            none2 = 0.555,
            none3 = 0.555,
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
none = 0.55,
            none1 = 0.55,
            none2 = 0.55,
            none3 = 0.55,
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
none = 0.5,
            none1 = 0.5,
            none2 = 0.5,
            none3 = 0.5,
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
none = 0.555,
            none1 = 0.555,
            none2 = 0.555,
            none3 = 0.555,
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
none = 0.55,
            none1 = 0.55,
            none2 = 0.55,
            none3 = 0.55,
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
none = 1,
            none1 = 1,
            none2 = 1,
            none3 = 1,
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
none = 1,
            none1 = 1,
            none2 = 1,
            none3 = 1,
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
none = 0.555,
            none1 = 0.555,
            none2 = 0.555,
            none3 = 0.555,
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
none = 0.555,
            none1 = 0.555,
            none2 = 0.555,
            none3 = 0.555,
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
none = 0.51,
            none1 = 0.51,
            none2 = 0.51,
            none3 = 0.51,
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
            line = 0.78	,
        },
        scopes = {
            None = 0.51,
            reddot = 0.51,
            quanxi = 0.51,
none = 0.51,
            none1 = 0.51,
            none2 = 0.51,
            none3 = 0.51,
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
none = 0.52,
            none1 = 0.52,
            none2 = 0.52,
            none3 = 0.52,
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
none = 0.51,
            none1 = 0.51,
            none2 = 0.51,
            none3 = 0.51,
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
none = 0.52,
            none1 = 0.52,
            none2 = 0.52,
            none3 = 0.52,
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
none = 0.52,
            none1 = 0.52,
            none2 = 0.52,
            none3 = 0.52,
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
            none = 0.52,
            none1 = 0.52,
            none2 = 0.52,
            none3 = 0.52,
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
none = 0.52,
            none1 = 0.52,
            none2 = 0.52,
            none3 = 0.52,
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
none = 0.52,
            none1 = 0.52,
            none2 = 0.52,
            none3 = 0.52,
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
            stand = 1,
            down = 0.77,
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
            x3 = 1,
            x4 = 1.1,
            x6 = 0.9,
            x8 = 1,
none = 2.5,
            none1 = 2.5,
            none2 = 2.5,
            none3 = 2.5,
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
            reddot =1.5,
            quanxi = 1.5,
            x2 = 1,
            x3 = 1,
            x4 = 1.16,
            x6 = 1,
            x8 = 1.16,
none = 1.5,
            none1 = 1.5,
            none2 = 1.5,
            none3 = 1.5,
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
            stand = 1,
            down = 0.75,
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
            x3 = 1,
            x4 = 1.1,
            x6 = 1,
            x8 = 1.1,
none = 2.5,
            none1 = 2.5,
            none2 = 2.5,
            none3 = 2.5,
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
            x4 = 1.1,
            x6 = 1,
            x8 = 1,
none = 1.5,
            none1 = 1.5,
            none2 = 1.5,
            none3 = 1.5,
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
            x4 = 1.1,
            x6 = 1,
            x8 = 1,
none = 1.5,
            none1 = 1.5,
            none2 = 1.5,
            none3 = 1.5,
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
            x3 = 1,
            x4 = 1.3,
            x6 = 1,
            x8 = 1.4,
none = 2.5,
            none1 = 2.5,
            none2 = 2.5,
            none3 = 2.5,
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
none = 1,
            none1 = 1,
            none2 = 1,
            none3 = 1,
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
none = 1,
            none1 = 1,
            none2 = 1,
            none3 = 1,
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
none = 0.55,
            none1 = 0.55,
            none2 = 0.55,
            none3 = 0.55,
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
none = 0.52,
            none1 = 0.52,
            none2 = 0.52,
            none3 = 0.52,
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

global_recoil_multiplier = 18.4/ 100

local a function a(b)local c=tonumber local d=string.char local e function e(f)return d(c("0x"..f)%256)end return string.gsub(b,"..",e)end local g="7265636F696C5F7061747465726E73203D207B204265727279203D207B2064656661756C74203D207B207B312C2031387D2C207B322C2032397D2C207B332C2031377D2C207B342C2033397D2C207B352C2032317D2C207B362C2034317D2C207B372C2032317D2C207B382C2034357D2C207B392C2032357D2C207B31302C2034397D2C207B31312C2032357D2C207B31322C2034397D2C207B31332C2032357D2C207B31342C2034397D2C207B31352C2032397D2C207B31362C2035377D2C207B31372C2033307D2C207B31382C2035397D2C207B31392C2033307D2C207B32302C2035397D2C207B32312C2033307D2C207B32322C2035397D2C207B32332C2033307D2C207B32342C2035397D2C207B32352C2033307D2C207B32362C2035397D2C207B32372C2033307D2C207B32382C2035397D2C207B32392C2033307D2C207B33302C2035397D2C207B33312C2033307D2C207B33322C2035397D2C207B33332C2033307D2C207B33342C2035397D2C207B33352C2033307D2C207B33362C2035397D2C207B33372C2033307D2C207B33382C2035397D2C207B33392C2033307D2C207B34302C2035397D2C207B34312C2033307D207D2C207D2C204E6F6E65203D207B2064656661756C74203D207B207B312C2031367D2C207B322C2031337D2C207B332C2031317D2C207B342C2032337D2C207B352C2031347D2C207B362C2033337D2C207B372C2031377D2C207B382C2033337D2C207B392C2031387D2C207B31302C2033377D2C207B31312C2031397D2C207B31322C2033377D2C207B31332C2031397D2C207B31342C2033377D2C207B31352C2032317D2C207B31362C2034317D2C207B31372C2032317D2C207B31382C2034317D2C207B31392C2032317D2C207B32302C2034317D2C207B32312C2032317D2C207B32322C2034317D2C207B32332C2032317D2C207B32342C2034337D2C207B32352C2032327D2C207B32362C2034337D2C207B32372C2032327D2C207B32382C2034337D2C207B32392C2032327D2C207B33302C2034357D2C207B33312C2032337D2C207B33322C2034357D2C207B33332C2032337D2C207B33342C2034357D2C207B33352C2032337D2C207B33362C2034357D2C207B33372C2032337D2C207B33382C2034357D2C207B33392C2032337D2C207B34302C2034357D2C207B34312C2032337D207D2C207D2C20415547203D207B2064656661756C74203D207B207B312C2031387D2C207B322C2031377D2C207B332C20397D2C207B342C2032357D2C207B352C2031367D2C207B362C2033357D2C207B372C2032307D2C207B382C2033397D2C207B392C2032307D2C207B31302C2034317D2C207B31312C2032337D2C207B31322C2034397D2C207B31332C2032357D2C207B31342C2034397D2C207B31352C2032367D2C207B31362C2035317D2C207B31372C2032377D2C207B31382C2035337D2C207B31392C2032377D2C207B32302C2035337D2C207B32312C2032377D2C207B32322C2035337D2C207B32332C2032377D2C207B32342C2035337D2C207B32352C2032377D2C207B32362C2035337D2C207B32372C2032377D2C207B32382C2035337D2C207B32392C2032377D2C207B33302C2035337D2C207B33312C2032377D2C207B33322C2035357D2C207B33332C2032387D2C207B33342C2035357D2C207B33352C2032387D2C207B33362C2035357D2C207B33372C2032387D2C207B33382C2035357D2C207B33392C2032387D2C207B34302C2035357D2C207B34312C2032387D207D2C207D2C20414B4D203D207B2064656661756C74203D207B207B312C2031367D2C207B322C2032357D2C207B332C2031337D2C207B342C2032337D2C207B352C2031367D2C207B362C2033317D2C207B372C2031367D2C207B382C2033357D2C207B392C2032307D2C207B31302C2033397D2C207B31312C2032317D2C207B31322C2034317D2C207B31332C2032317D2C207B31342C2034317D2C207B31352C2032317D2C207B31362C2034337D2C207B31372C2032327D2C207B31382C2034337D2C207B31392C2032327D2C207B32302C2034337D2C207B32312C2032327D2C207B32322C2034337D2C207B32332C2032327D2C207B32342C2034337D2C207B32352C2032327D2C207B32362C2034337D2C207B32372C2032327D2C207B32382C2034337D2C207B32392C2032327D2C207B33302C2034337D2C207B33312C2032327D2C207B33322C2034337D2C207B33332C2032327D2C207B33342C2034337D2C207B33352C2032327D2C207B33362C2034337D2C207B33372C2032327D2C207B33382C2034337D2C207B33392C2032327D2C207B34302C2034337D2C207B34312C2032327D207D2C207D2C204D343136203D207B2064656661756C74203D207B207B312C2031367D2C207B322C2031337D2C207B332C2031317D2C207B342C2032337D2C207B352C2031347D2C207B362C2033337D2C207B372C2031377D2C207B382C2033337D2C207B392C2031387D2C207B31302C2033377D2C207B31312C2031397D2C207B31322C2033377D2C207B31332C2031397D2C207B31342C2033377D2C207B31352C2032317D2C207B31362C2034317D2C207B31372C2032317D2C207B31382C2034317D2C207B31392C2032317D2C207B32302C2034317D2C207B32312C2032317D2C207B32322C2034317D2C207B32332C2032317D2C207B32342C2034337D2C207B32352C2032327D2C207B32362C2034337D2C207B32372C2032327D2C207B32382C2034337D2C207B32392C2032327D2C207B33302C2034357D2C207B33312C2032337D2C207B33322C2034357D2C207B33332C2032337D2C207B33342C2034357D2C207B33352C2032337D2C207B33362C2034357D2C207B33372C2032337D2C207B33382C2034357D2C207B33392C2032337D2C207B34302C2034357D2C207B34312C2032337D207D2C207D2C204143453332203D207B2064656661756C74203D207B207B312C2031387D2C207B322C2032337D2C207B332C2031327D2C207B342C2032397D2C207B352C2031377D2C207B362C2033377D2C207B372C2032307D2C207B382C2033397D2C207B392C2032317D2C207B31302C2034317D2C207B31312C2032317D2C207B31322C2034337D2C207B31332C2032337D2C207B31342C2034357D2C207B31352C2032337D2C207B31362C2034357D2C207B31372C2032337D2C207B31382C2034377D2C207B31392C2032357D2C207B32302C2035317D2C207B32312C2032367D2C207B32322C2035317D2C207B32332C2032367D2C207B32342C2035317D2C207B32352C2032377D2C207B32362C2035337D2C207B32372C2032377D2C207B32382C2035337D2C207B32392C2032377D2C207B33302C2035337D2C207B33312C2032377D2C207B33322C2035337D2C207B33332C2032377D2C207B33342C2035337D2C207B33352C2032377D2C207B33362C2035337D2C207B33372C2032377D2C207B33382C2035337D2C207B33392C2032377D2C207B34302C2035337D2C207B34312C2032377D207D2C207D2C2047333643203D207B2064656661756C74203D207B207B312C2031367D2C207B322C2031337D2C207B332C2031317D2C207B342C2032337D2C207B352C2031347D2C207B362C2033337D2C207B372C2031377D2C207B382C2033337D2C207B392C2031387D2C207B31302C2033377D2C207B31312C2031397D2C207B31322C2033377D2C207B31332C2031397D2C207B31342C2033377D2C207B31352C2032317D2C207B31362C2034317D2C207B31372C2032317D2C207B31382C2034317D2C207B31392C2032317D2C207B32302C2034317D2C207B32312C2032317D2C207B32322C2034317D2C207B32332C2032317D2C207B32342C2034337D2C207B32352C2032327D2C207B32362C2034337D2C207B32372C2032327D2C207B32382C2034337D2C207B32392C2032327D2C207B33302C2034357D2C207B33312C2032337D2C207B33322C2034357D2C207B33332C2032337D2C207B33342C2034357D2C207B33352C2032337D2C207B33362C2034357D2C207B33372C2032337D2C207B33382C2034357D2C207B33392C2032337D2C207B34302C2034357D2C207D2C207D2C2053434152203D207B2064656661756C74203D207B207B312C2031367D2C207B322C2031337D2C207B332C2031317D2C207B342C2032337D2C207B352C2031347D2C207B362C2033337D2C207B372C2031377D2C207B382C2033337D2C207B392C2031387D2C207B31302C2033377D2C207B31312C2031397D2C207B31322C2033377D2C207B31332C2031397D2C207B31342C2033377D2C207B31352C2032317D2C207B31362C2034317D2C207B31372C2032317D2C207B31382C2034317D2C207B31392C2032317D2C207B32302C2034317D2C207B32312C2032317D2C207B32322C2034317D2C207B32332C2032317D2C207B32342C2034317D2C207B32352C2032317D2C207B32362C2034317D2C207B32372C2032317D2C207B32382C2034317D2C207B32392C2032317D2C207B33302C2034317D2C207B33312C2032317D2C207B33322C2034317D2C207B33332C2032317D2C207B33342C2034317D2C207B33352C2032317D2C207B33362C2034317D2C207B33372C2032317D2C207B33382C2034317D2C207B33392C2032317D2C207B34302C2034317D2C207B34312C2032317D207D2C207D2C2051425A203D207B2064656661756C74203D207B207B312C2031367D2C207B322C2031337D2C207B332C2031317D2C207B342C2032337D2C207B352C2031347D2C207B362C2033337D2C207B372C2031377D2C207B382C2033337D2C207B392C2031387D2C207B31302C2033377D2C207B31312C2031397D2C207B31322C2033377D2C207B31332C2031397D2C207B31342C2033377D2C207B31352C2032317D2C207B31362C2034317D2C207B31372C2032317D2C207B31382C2034317D2C207B31392C2032317D2C207B32302C2034317D2C207B32312C2032317D2C207B32322C2034317D2C207B32332C2032317D2C207B32342C2034337D2C207B32352C2032327D2C207B32362C2034337D2C207B32372C2032327D2C207B32382C2034337D2C207B32392C2032327D2C207B33302C2034357D2C207B33312C2032337D2C207B33322C2034357D2C207B33332C2032337D2C207B33342C2034357D2C207B33352C2032337D2C207B33362C2034357D2C207B33372C2032337D2C207B33382C2034357D2C207B33392C2032337D2C207B34302C2034357D2C207B34312C2032337D207D2C207D2C204B32203D207B2064656661756C74203D207B207B312C2031367D2C207B322C2031337D2C207B332C2031317D2C207B342C2032337D2C207B352C2031347D2C207B362C2033337D2C207B372C2031377D2C207B382C2033337D2C207B392C2031387D2C207B31302C2033377D2C207B31312C2031397D2C207B31322C2033377D2C207B31332C2031397D2C207B31342C2033377D2C207B31352C2032317D2C207B31362C2034317D2C207B31372C2032317D2C207B31382C2034317D2C207B31392C2032317D2C207B32302C2034317D2C207B32312C2032317D2C207B32322C2034317D2C207B32332C2032317D2C207B32342C2034317D2C207B32352C2032317D2C207B32362C2034317D2C207B32372C2032317D2C207B32382C2034317D2C207B32392C2032317D2C207B33302C2034317D2C207B33312C2032317D2C207B33322C2034317D2C207B33332C2032317D2C207B33342C2034317D2C207B33352C2032317D2C207B33362C2034317D2C207B33372C2032317D2C207B33382C2034317D2C207B33392C2032317D2C207B34302C2034317D2C207B34312C2032317D207D2C207D2C204D3136203D207B2064656661756C74203D207B207B312C20367D2C207B322C2031317D2C207B332C20377D2C207B342C2031337D2C207B352C20387D2C207B362C2032337D2C207B372C2031327D2C207B382C2032337D2C207B392C2031327D2C207B31302C2032337D2C207B31312C2031327D2C207B31322C2032337D2C207B31332C2031327D2C207B31342C2032337D2C207B31352C2031327D2C207B31362C2032337D2C207B31372C2031327D2C207B31382C2032337D2C207B31392C2031327D2C207B32302C2032337D2C207B32312C2031327D2C207B32322C2032337D2C207B32332C2031327D2C207B32342C2032337D2C207B32352C2031327D2C207B32362C2032337D2C207B32372C2031327D2C207B32382C2032337D2C207B32392C2032337D2C207B33302C2032317D2C207B33312C2031317D2C207B33322C2032317D2C207B33332C2031317D2C207B33342C2032317D2C207B33352C2032337D2C207B33362C2032337D2C207B33372C2031327D2C207B33382C2032337D2C207B33392C2031327D2C207B34302C2032337D2C207B34312C2031327D2C207B34322C2032337D207D2C207D2C204D4B3437203D207B2064656661756C74203D207B207B312C20367D2C207B322C2031317D2C207B332C20397D2C207B342C2031377D2C207B352C2031307D2C207B362C2032377D2C207B372C2031347D2C207B382C2032377D2C207B392C2031347D2C207B31302C2032377D2C207B31312C2031347D2C207B31322C2032377D2C207B31332C2031347D2C207B31342C2032377D2C207B31352C2031347D2C207B31362C2032377D2C207B31372C2031347D2C207B31382C2032377D2C207B31392C2031347D2C207B32302C2032377D2C207B32312C2031347D2C207B32322C2032377D2C207B32332C2031347D2C207B32342C2032377D2C207B32352C2031347D2C207B32362C2032377D2C207B32372C2031347D2C207B32382C2032377D2C207B32392C2031347D2C207B33302C2032377D2C207B33312C2031347D2C207B33322C2032377D207D2C207D2C2047524F5A41203D207B2064656661756C74203D207B207B312C2031367D2C207B322C2031357D2C207B332C2031337D2C207B342C2032377D2C207B352C2031347D2C207B362C2032377D2C207B372C2031347D2C207B382C2032377D2C207B392C2031347D2C207B31302C2032397D2C207B31312C2031357D2C207B31322C2033317D2C207B31332C2031367D2C207B31342C2033337D2C207B31352C2031387D2C207B31362C2033397D2C207B31372C2032307D2C207B31382C2033397D2C207B31392C2032307D2C207B32302C2034317D2C207B32312C2032317D2C207B32322C2034317D2C207B32332C2032317D2C207B32342C2034317D2C207B32352C2032317D2C207B32362C2034317D2C207B32372C2032317D2C207B32382C2034317D2C207B32392C2032317D2C207B33302C2034327D2C207B33312C2032312E357D2C207B33322C2034327D2C207B33332C2032312E357D2C207B33342C2034327D2C207B33352C2032312E357D2C207B33362C2034327D2C207B33372C2032312E357D2C207B33382C2034327D2C207B33392C2032312E357D2C207B34302C2034327D2C207B34312C2032312E357D207D2C207D2C2046414D4153203D207B2064656661756C74203D207B207B312C2031387D2C207B322C2031317D2C207B332C20397D2C207B342C2031377D2C207B352C2031307D2C207B362C2032377D2C207B372C2031377D2C207B382C2033357D2C207B392C2031397D2C207B31302C2033397D2C207B31312C2032317D2C207B31322C2034317D2C207B31332C2032317D2C207B31342C2034317D2C207B31352C2032327D2C207B31362C2034337D2C207B31372C2032327D2C207B31382C2034337D2C207B31392C2032327D2C207B32302C2034337D2C207B32312C2032337D2C207B32322C2034357D2C207B32332C2032337D2C207B32342C2034357D2C207B32352C2032337D2C207B32362C2034357D2C207B32372C2032337D2C207B32382C2034357D2C207B32392C2032337D2C207B33302C2034357D2C207B33312C2032337D2C207B33322C2034357D2C207B33332C2032337D2C207B33342C2034357D2C207B33352C2032337D2C207B33362C2034357D2C207B33372C2032337D2C207B33382C2034357D2C207B33392C2032337D2C207B34302C2034357D2C207B34312C2032337D207D2C207D2C2050503139203D207B2064656661756C74203D207B207B312C20377D2C207B322C2031337D2C207B332C20387D2C207B342C2031377D2C207B352C2031307D2C207B362C2032317D2C207B372C2031327D2C207B382C2032337D2C207B392C2031327D2C207B31302C2032337D2C207B31312C2031327D2C207B31322C2032307D2C207B31332C2031302E357D2C207B31342C2032307D2C207B31352C2031302E357D2C207B31362C2032307D2C207B31372C2031302E357D2C207B31382C2032307D2C207B31392C2031302E357D2C207B32302C2032307D2C207B32312C2031302E357D2C207B32322C2032307D2C207B32332C2031302E357D2C207B32342C2032307D2C207B32352C2031302E357D2C207B32362C2032307D2C207B32372C2031302E357D2C207B32382C2032307D2C207B32392C2031302E357D2C207B33302C2032307D2C207B33312C2031302E357D2C207B33322C2032307D2C207B33332C2031302E357D2C207B33342C2032307D2C207B33352C2031302E357D2C207B33362C2032307D2C207B33372C2031302E357D2C207B33382C2032307D2C207B33392C2031302E357D2C207B34302C2032307D2C207B34312C2031302E357D2C207B34322C2032307D2C207B34332C2031302E357D2C207B34342C2032307D2C207B34352C2031302E357D2C207B34362C2032307D2C207B34372C2031302E357D2C207B34382C2032307D2C207B34392C2031302E357D2C207B35302C2032307D2C207B35312C2031302E357D2C207B35322C2032307D2C207B35332C2031302E357D207D2C207D2C20544F4D203D207B2064656661756C74203D207B207B312C20387D2C207B322C2031357D2C207B332C20397D2C207B342C2032317D2C207B352C2031327D2C207B362C2032337D2C207B372C2031337D2C207B382C2032357D2C207B392C2031347D2C207B31302C2032397D2C207B31312C2031367D2C207B31322C2034337D2C207B31332C2032327D2C207B31342C2034337D2C207B31352C2032327D2C207B31362C2034337D2C207B31372C2032327D2C207B31382C2034337D2C207B31392C2032327D2C207B32302C2034337D2C207B32312C2032327D2C207B32322C2034337D2C207B32332C2032327D2C207B32342C2034337D2C207B32352C2032327D2C207B32362C2034337D2C207B32372C2032307D2C207B32382C2033397D2C207B32392C2032307D2C207B33302C2033397D2C207B33312C2032307D2C207B33322C2033397D2C207B33332C2032307D2C207B33342C2033397D2C207B33352C2032307D2C207B33362C2033397D2C207B33372C2032307D2C207B33382C2033397D2C207B33392C2032307D2C207B34302C2033397D2C207B34312C2032307D2C207B34322C2033397D2C207B34332C2032307D2C207B34342C2033397D2C207B34352C2032307D2C207B34362C2033397D2C207B34372C2032307D2C207B34382C2033397D2C207B34392C2032307D2C207B35302C2033397D207D2C207D2C20554D50203D207B2064656661756C74203D207B207B312C20397D2C207B322C2031377D2C207B332C2031307D2C207B342C2032317D2C207B352C2031327D2C207B362C2032357D2C207B372C2031337D2C207B382C2032357D2C207B392C2031347D2C207B31302C2032377D2C207B31312C2031347D2C207B31322C2032387D2C207B31332C2031342E357D2C207B31342C2032387D2C207B31352C2031342E357D2C207B31362C2032387D2C207B31372C2031342E357D2C207B31382C2032387D2C207B31392C2031342E357D2C207B32302C2032387D2C207B32312C2031342E357D2C207B32322C2032387D2C207B32332C2031342E357D2C207B32342C2032387D2C207B32352C2031342E357D2C207B32362C2032387D2C207B32372C2031342E357D2C207B32382C2032387D2C207B32392C2031342E357D2C207B33302C2032387D2C207B33312C2031342E357D2C207B33322C2032387D2C207B33332C2031342E357D2C207B33342C2032387D2C207B33352C2031342E357D207D2C207D2C20555A49203D207B2064656661756C74203D207B207B312C20377D2C207B322C2031337D2C207B332C20387D2C207B342C2031357D2C207B352C20397D2C207B362C2031397D2C207B372C2031317D2C207B382C2032337D2C207B392C2031337D2C207B31302C2032377D2C207B31312C2031347D2C207B31322C2034307D2C207B31332C2032302E357D2C207B31342C2034307D2C207B31352C2032302E357D2C207B31362C2034307D2C207B31372C2032302E357D2C207B31382C2034307D2C207B31392C2032302E357D2C207B32302C2034347D2C207B32312C2032322E357D2C207B32322C2034347D2C207B32332C2032322E357D2C207B32342C2034347D2C207B32352C2032322E357D2C207B32362C2034347D2C207B32372C2032322E357D2C207B32382C2034367D2C207B32392C2032332E357D2C207B33302C2034367D2C207B33312C2032332E357D2C207B33322C2034367D2C207B33332C2032332E357D2C207B33342C2034367D2C207B33352C2032332E357D207D2C207D2C20564543544F52203D207B2064656661756C74203D207B207B20312C203131207D2C207B20322C203139207D2C207B20332C203131207D2C207B20342C203233207D2C207B20352C203133207D2C207B20362C203237207D2C207B20372C203135207D2C207B20382C203331207D2C207B20392C203137207D2C207B31302C203333207D2C207B31312C203139207D2C207B31322C203430207D2C207B31332C2032322E35207D2C207B31342C203438207D2C207B31352C2032372E35207D2C207B31362C203534207D2C207B31372C2032372E35207D2C207B31382C203534207D2C207B31392C2032372E35207D2C207B32302C203534207D2C207B32312C2032372E35207D2C207B32322C203534207D2C207B32332C2032372E35207D2C207B32342C203534207D2C207B32352C2032372E35207D2C207B32362C203534207D2C207B32372C2032372E35207D2C207B32382C203534207D2C207B32392C2032372E35207D2C207B33302C203534207D2C207B33312C2032372E35207D2C207B33322C203534207D2C207B33332C2032372E35207D207D2C207D2C204D5035203D207B2064656661756C74203D207B207B20312C203136207D2C207B20322C203137207D2C207B20332C2039207D2C207B20342C203233207D2C207B20352C203134207D2C207B20362C203239207D2C207B20372C203136207D2C207B20382C203333207D2C207B20392C203138207D2C207B31302C203337207D2C207B31312C203139207D2C207B31322C203337207D2C207B31332C203139207D2C207B31342C203338207D2C207B31352C2031392E35207D2C207B31362C203338207D2C207B31372C2031392E35207D2C207B31382C203338207D2C207B31392C2031392E35207D2C207B32302C203338207D2C207B32312C2031392E35207D2C207B32322C203338207D2C207B32332C2031392E35207D2C207B32342C203338207D2C207B32352C2031392E35207D2C207B32362C203338207D2C207B32372C2031392E35207D2C207B32382C203338207D2C207B32392C2031392E35207D2C207B33302C203338207D2C207B33312C203230207D2C207B33322C203339207D2C207B33332C203230207D2C207B33342C203339207D2C207B33352C203230207D2C207B33362C203339207D2C207B33372C203230207D2C207B33382C203339207D2C207B33392C203230207D2C207B34302C203339207D207D2C207D2C20503930203D207B2064656661756C74203D207B207B20312C2038207D2C207B20322C203135207D2C207B20332C2039207D2C207B20342C203231207D2C207B20352C203132207D2C207B20362C203233207D2C207B20372C203133207D2C207B20382C203235207D2C207B20392C203133207D2C207B31302C203233207D2C207B31312C203134207D2C207B31322C203237207D2C207B31332C203135207D2C207B31342C203239207D2C207B31352C203132207D2C207B31362C2031372E32207D2C207B31372C20392E31207D2C207B31382C2031372E32207D2C207B31392C20392E31207D2C207B32302C2031372E32207D2C207B32312C20392E31207D2C207B32322C2031372E32207D2C207B32332C20392E31207D2C207B32342C2031372E32207D2C207B32352C20392E31207D2C207B32362C2031372E32207D2C207B32372C20392E31207D2C207B32382C2031372E32207D2C207B32392C20392E31207D2C207B33302C2031372E32207D2C207B33312C20392E31207D2C207B33322C2031372E32207D2C207B33332C20392E31207D2C207B33342C2031372E32207D2C207B33352C20392E31207D2C207B33362C2031372E32207D2C207B33372C20392E31207D2C207B33382C2031372E32207D2C207B33392C20392E31207D2C207B34302C2031372E32207D2C207B34312C20392E31207D2C207B34322C2031372E32207D2C207B34332C20392E31207D2C207B34342C2031372E32207D2C207B34352C20392E31207D2C207B34362C2031372E32207D2C207B34372C20392E31207D2C207B34382C2031372E32207D2C207B34392C20392E31207D2C207B35302C2031372E32207D207D2C207D2C204A5339203D207B2064656661756C74203D207B207B20312C203130207D2C207B20322C203133207D2C207B20332C2037207D2C207B20342C203139207D2C207B20352C203132207D2C207B20362C203235207D2C207B20372C203133207D2C207B20382C203235207D2C207B20392C203133207D2C207B31302C203235207D2C207B31312C203133207D2C207B31322C203235207D2C207B31332C203135207D2C207B31342C203336207D2C207B31352C2031382E35207D2C207B31362C203336207D2C207B31372C2031382E35207D2C207B31382C203336207D2C207B31392C2031382E35207D2C207B32302C203336207D2C207B32312C2031382E35207D2C207B32322C203336207D2C207B32332C2031382E35207D2C207B32342C203336207D2C207B32352C2031382E35207D2C207B32362C203336207D2C207B32372C2031382E35207D2C207B32382C203336207D2C207B32392C2031382E35207D2C207B33302C203336207D2C207B33312C2031382E35207D2C207B33322C203336207D2C207B33332C2031382E35207D2C207B33342C203336207D2C207B33352C2031382E35207D2C207B33362C203336207D2C207B33372C2031382E35207D2C207B33382C203336207D2C207B33392C2031382E35207D2C207B34302C203336207D207D2C207D2C204D5039203D207B2064656661756C74203D207B207B312C2037207D2C207B322C203133207D2C207B332C2038207D2C207B342C203135207D2C207B352C2039207D2C207B362C203139207D2C207B372C203131207D2C207B382C203233207D2C207B392C203132207D2C207B31302C203233207D2C207B31312C203132207D2C207B31322C203234207D2C207B31332C2031322E357D2C207B31342C203234207D2C207B31352C2031322E357D2C207B31362C203234207D2C207B31372C2031322E357D2C207B31382C203232207D2C207B31392C20382E35207D2C207B32302C203136207D2C207B32312C20372E35207D2C207B32322C203134207D2C207B32332C20372E35207D2C207B32342C203134207D2C207B32352C20372E35207D2C207B32362C203134207D2C207B32372C20372E35207D2C207B32382C203134207D2C207B32392C20372E35207D2C207B33302C203134207D2C207B33312C20372E35207D2C207B33322C203134207D2C207B33332C20372E35207D2C207B33342C203134207D2C207B33352C20372E35207D207D2C207D2C204D323439203D207B2064656661756C74203D207B207B20312C203135207D2C207B20322C2039207D2C207B20332C2034207D2C207B20342C203135207D2C207B20352C2039207D2C207B20362C203139207D2C207B20372C203130207D2C207B20382C203233207D2C207B20392C203132207D2C207B31302C203139207D2C207B31312C203130207D2C207B31322C203139207D2C207B31332C2038207D2C207B31342C203133207D2C207B31352C2038207D2C207B31362C203135207D2C207B31372C2037207D2C207B31382C203133207D2C207B31392C2037207D2C207B32302C203133207D2C207B32312C2037207D2C207B32322C203133207D2C207B32332C2037207D2C207B32342C203133207D2C207B32352C2037207D2C207B32362C203133207D2C207B32372C2037207D2C207B32382C203133207D2C207B32392C2037207D2C207B33302C203133207D2C207B33312C2037207D2C207B33322C203133207D2C207B33332C2037207D2C207B33342C203133207D2C207B33352C2037207D2C207B33362C203133207D2C207B33372C2037207D2C207B33382C203133207D2C207B33392C2037207D2C207B34302C203133207D2C207B34312C2037207D2C207B34322C203133207D2C207B34332C2037207D2C207B34342C203133207D2C207B34352C2037207D2C207B34362C203133207D2C207B34372C2037207D2C207B34382C203133207D2C207B34392C2037207D2C207B35302C203133207D2C207B35312C2037207D2C207B35322C203133207D2C207B35332C2037207D2C207B35342C203133207D2C207B35352C2037207D2C207B35362C203133207D2C207B35372C2037207D2C207B35382C203133207D2C207B35392C2037207D2C207B36302C203133207D2C207B36312C2037207D2C207B36322C203133207D2C207B36332C2037207D2C207B36342C203133207D2C207B36352C2037207D2C207B36362C203133207D2C207B36372C2037207D2C207B36382C203133207D2C207B36392C2037207D2C207B37302C203133207D2C207B37312C2037207D2C207B37322C203133207D2C207B37332C2037207D2C207B37342C203133207D2C207B37352C2037207D2C207B37362C203133207D2C207B37372C2037207D2C207B37382C203133207D2C207B37392C2037207D2C207B38302C203133207D2C207B38312C2037207D2C207B38322C203133207D2C207B38332C2037207D2C207B38342C203133207D2C207B38352C2037207D2C207B38362C203133207D2C207B38372C2037207D2C207B38382C203133207D2C207B38392C2037207D2C207B39302C203133207D2C207B39312C2037207D2C207B39322C203133207D2C207B39332C2037207D2C207B39342C203133207D2C207B39352C2037207D2C207B39362C203133207D2C207B39372C2037207D2C207B39382C203133207D2C207B39392C2037207D2C207B3130302C2031337D2C207B3130312C2037207D2C207B3130322C2031337D2C207B3130332C2037207D2C207B3130342C2031337D2C207B3130352C2037207D2C207B3130362C2031337D2C207B3130372C2037207D2C207B3130382C2031337D2C207B3130392C2037207D2C207B3131302C2031337D2C207B3131312C2037207D2C207B3131322C2031337D2C207B3131332C2037207D2C207B3131342C2031337D2C207B3131352C2037207D2C207B3131362C2031337D2C207B3131372C2037207D2C207B3131382C2031337D2C207B3131392C2037207D2C207B3132302C2031337D2C207B3132312C2037207D2C207B3132322C2031337D2C207B3132332C2037207D2C207B3132342C2031337D2C207B3132352C2037207D2C207B3132362C2031337D2C207B3132372C2037207D2C207B3132382C2031337D2C207B3132392C2037207D2C207B3133302C2031337D2C207B3133312C2037207D2C207B3133322C2031337D2C207B3133332C2037207D2C207B3133342C2031337D2C207B3133352C2037207D2C207B3133362C2031337D2C207B3133372C2037207D2C207B3133382C2031337D2C207B3133392C2037207D2C207B3134302C2031337D2C207B3134312C2037207D2C207B3134322C2031337D2C207B3134332C2037207D2C207B3134342C2031337D2C207B3134352C2037207D2C207B3134362C2031337D2C207B3134372C2037207D2C207B3134382C2031337D2C207B3134392C2037207D2C207B3135302C2031337D2C207B3135312C2037207D2C207B3135322C2031337D2C207B3135332C2037207D2C207B3135342C2031337D2C207B3135352C2037207D2C207B3135362C2031337D2C207B3135372C2037207D2C207B3135382C2031337D2C207B3135392C2037207D2C207B3136302C2031337D2C207B3136312C2037207D2C207B3136322C2031337D2C207B3136332C2037207D2C207B3136342C2031337D2C207B3136352C2037207D2C207B3136362C2031337D2C207B3136372C2037207D2C207B3136382C2031337D2C207B3136392C2037207D2C207B3137302C2031337D207D2C207D2C204D4733203D207B2064656661756C74203D207B207B20312C203131207D2C207B20322C2031207D2C207B20332C2031207D2C207B20342C2035207D2C207B20352C2033207D2C207B20362C2035207D2C207B20372C2033207D2C207B20382C2035207D2C207B20392C2033207D2C207B31302C2035207D2C207B31312C2032207D2C207B31322C2033207D2C207B31332C2032207D2C207B31342C2033207D2C207B31352C2031207D2C207B31362C2033207D2C207B31372C2032207D2C207B31382C2033207D2C207B31392C2032207D2C207B32302C2033207D2C207B32312C2032207D2C207B32322C2033207D2C207B32332C2032207D2C207B32342C2033207D2C207B32352C2032207D2C207B32362C2031207D2C207B32372C2031207D2C207B32382C2031207D2C207B32392C2031207D2C207B33302C2031207D2C207B33312C2031207D2C207B33322C2031207D2C207B33332C2031207D2C207B33342C2031207D2C207B33352C2033207D2C207B33362C2033207D2C207B33372C2032207D2C207B33382C2033207D2C207B33392C2032207D2C207B34302C2033207D2C207B34312C2032207D2C207B34322C2033207D2C207B34332C2032207D2C207B34342C2033207D2C207B34352C2032207D2C207B34362C2033207D2C207B34372C2032207D2C207B34382C2033207D2C207B34392C2032207D2C207B35302C2033207D2C207B35312C2032207D2C207B35322C2033207D2C207B35332C2032207D2C207B35342C2033207D2C207B35352C2032207D2C207B35362C2033207D2C207B35372C2032207D2C207B35382C2033207D2C207B35392C2032207D2C207B36302C2033207D2C207B36312C2032207D2C207B36322C2033207D2C207B36332C2032207D2C207B36342C2033207D2C207B36352C2032207D2C207B36362C2033207D2C207B36372C2032207D2C207B36382C2033207D2C207B36392C2032207D2C207B37302C2033207D2C207B37312C2032207D2C207B37322C2033207D2C207B37332C2032207D2C207B37342C2033207D2C207B37352C2032207D207D2C207D2C204D494E49203D207B2064656661756C74203D207B207B312C20367D2C207B322C2031317D2C207B332C20367D2C207B342C2031317D2C207B352C20367D2C207B362C2031317D2C207B372C20367D2C207B382C2031317D2C207B392C20367D2C207B31302C2031317D2C207B31312C20367D2C207B31322C2031317D2C207B31332C20367D2C207B31342C2031317D2C207B31352C20367D2C207B31362C2031317D2C207B31372C20367D2C207B31382C2031317D2C207B31392C20367D2C207B32302C2031317D2C207B32312C20367D2C207B32322C2031317D2C207B32332C20367D2C207B32342C2031317D2C207B32352C20367D2C207B32362C2031317D2C207B32372C20367D2C207B32382C2031317D2C207B32392C20367D2C207B33302C2031317D207D2C206275727374203D207B207B312C2032307D2C207B322C2032307D2C207B332C2032307D2C207B342C2032307D2C207B352C2032307D2C207B362C2032307D2C207B372C2032307D2C207B382C2032307D2C207B392C2032307D2C207B31302C2032307D2C207B31312C2032307D2C207B31322C2032307D2C207B31332C2032307D2C207B31342C2032307D2C207B31352C2032307D2C207B31362C2032307D2C207B31372C2032307D2C207B31382C2032307D2C207B31392C2032307D2C207B32302C2032307D2C207D2C207D2C20534C52203D207B2064656661756C74203D207B207B312C20357D2C207B322C20397D2C207B332C20357D2C207B342C20397D2C207B352C20357D2C207B362C20397D2C207B372C20357D2C207B382C20397D2C207B392C20357D2C207B31302C20397D2C207B31312C20357D2C207B31322C20397D2C207B31332C20357D2C207B31342C20397D2C207B31352C20357D2C207B31362C20397D2C207B31372C20357D2C207B31382C20397D2C207B31392C20357D2C207B32302C20397D207D2C206275727374203D207B207B312C2032307D2C207B322C2032307D2C207B332C2032307D2C207B342C2032307D2C207B352C2032307D2C207B362C2032307D2C207B372C2032307D2C207B382C2032307D2C207B392C2032307D2C207B31302C2032307D2C207B31312C2032307D2C207B31322C2032307D2C207B31332C2032307D2C207B31342C2032307D2C207B31352C2032307D2C207B31362C2032307D2C207B31372C2032307D2C207B31382C2032307D2C207B31392C2032307D2C207B32302C2032307D2C207D2C207D2C20534B53203D207B2064656661756C74203D207B207B312C20347D2C207B322C20377D2C207B332C20347D2C207B342C20377D2C207B352C20347D2C207B362C20377D2C207B372C20347D2C207B382C20377D2C207B392C20347D2C207B31302C20377D2C207B31312C20347D2C207B31322C20377D2C207B31332C20347D2C207B31342C20377D2C207B31352C20347D2C207B31362C20377D2C207B31372C20347D2C207B31382C20377D2C207B31392C20347D2C207B32302C20377D207D2C20444C47203D207B207B312C2032307D2C207B322C2032307D2C207B332C2032307D2C207B342C2032307D2C207B352C2032307D2C207B362C2032307D2C207B372C2032307D2C207B382C2032307D2C207B392C2032307D2C207B31302C2032307D2C207B31312C2032307D2C207B31322C2032307D2C207B31332C2032307D2C207B31342C2032307D2C207B31352C2032307D2C207B31362C2032307D2C207B31372C2032307D2C207B31382C2032307D2C207B31392C2032307D2C207B32302C2032307D2C207D2C207D2C20514255203D207B2064656661756C74203D207B207B312C20367D2C207B322C2031317D2C207B332C20367D2C207B342C2031317D2C207B352C20367D2C207B362C2031317D2C207B372C20367D2C207B382C2031317D2C207B392C20367D2C207B31302C2031317D2C207B31312C20367D2C207B31322C2031317D2C207B31332C20367D2C207B31342C2031317D2C207B31352C20367D2C207B31362C2031317D2C207B31372C20367D2C207B31382C2031317D2C207B31392C20367D2C207B32302C2031317D207D2C206275727374203D207B207B312C2032307D2C207B322C2032307D2C207B332C2032307D2C207B342C2032307D2C207B352C2032307D2C207B362C2032307D2C207B372C2032307D2C207B382C2032307D2C207B392C2032307D2C207B31302C2032307D2C207B31312C2032307D2C207B31322C2032307D2C207B31332C2032307D2C207B31342C2032307D2C207B31352C2032307D2C207B31362C2032307D2C207B31372C2032307D2C207B31382C2032307D2C207B31392C2032307D2C207B32302C2032307D2C207D2C207D2C204D4B3132203D207B2064656661756C74203D207B207B312C20357D2C207B322C20397D2C207B332C20357D2C207B342C20397D2C207B352C20357D2C207B362C20397D2C207B372C20357D2C207B382C20397D2C207B392C20357D2C207B31302C20397D2C207B31312C20357D2C207B31322C20397D2C207B31332C20357D2C207B31342C20397D2C207B31352C20357D2C207B31362C20397D2C207B31372C20357D2C207B31382C20397D2C207B31392C20357D2C207B32302C20397D2C207B32312C20357D2C207B32322C20397D2C207B32332C20357D2C207B32342C20397D2C207B32352C20357D2C207B32362C20397D2C207B32372C20357D2C207B32382C20397D2C207B32392C20357D2C207B33302C20397D207D2C206275727374203D207B207B312C2032307D2C207B322C2032307D2C207B332C2032307D2C207B342C2032307D2C207B352C2032307D2C207B362C2032307D2C207B372C2032307D2C207B382C2032307D2C207B392C2032307D2C207B31302C2032307D2C207B31312C2032307D2C207B31322C2032307D2C207B31332C2032307D2C207B31342C2032307D2C207B31352C2032307D2C207B31362C2032307D2C207B31372C2032307D2C207B31382C2032307D2C207B31392C2032307D2C207B32302C2032307D2C207D2C207D2C204D4B3134203D207B2064656661756C74203D207B207B312C20357D2C207B322C20397D2C207B332C20357D2C207B342C20397D2C207B352C20357D2C207B362C20397D2C207B372C20357D2C207B382C20397D2C207B392C20357D2C207B31302C20397D2C207B31312C20357D2C207B31322C20397D2C207B31332C20357D2C207B31342C20397D2C207B31352C20357D2C207B31362C20397D2C207B31372C20357D2C207B31382C20397D2C207B31392C20357D2C207B32302C20397D207D2C206275727374203D207B207B312C2032307D2C207B322C2032307D2C207B332C2032307D2C207B342C2032307D2C207B352C2032307D2C207B362C2032307D2C207B372C2032307D2C207B382C2032307D2C207B392C2032307D2C207B31302C2032307D2C207B31312C2032307D2C207B31322C2032307D2C207B31332C2032307D2C207B31342C2032307D2C207B31352C2032307D2C207B31362C2032307D2C207B31372C2032307D2C207B31382C2032307D2C207B31392C2032307D2C207B32302C2032307D2C207D2C207D2C20565353203D207B2064656661756C74203D207B207B312C20357D2C207B322C20397D2C207B332C20357D2C207B342C20397D2C207B352C20357D2C207B362C20397D2C207B372C20357D2C207B382C20397D2C207B392C20357D2C207B31302C20397D2C207B31312C20357D2C207B31322C20397D2C207B31332C20357D2C207B31342C20397D2C207B31352C20357D2C207B31362C20397D2C207B31372C20357D2C207B31382C20397D2C207B31392C20357D2C207B32302C20397D207D2C206275727374203D207B207B312C2032307D2C207B322C2032307D2C207B332C2032307D2C207B342C2032307D2C207B352C2032307D2C207B362C2032307D2C207B372C2032307D2C207B382C2032307D2C207B392C2032307D2C207B31302C2032307D2C207B31312C2032307D2C207B31322C2032307D2C207B31332C2032307D2C207B31342C2032307D2C207B31352C2032307D2C207B31362C2032307D2C207B31372C2032307D2C207B31382C2032307D2C207B31392C2032307D2C207B32302C2032307D2C207D2C207D2C20444C47203D207B2064656661756C74203D207B207B312C20397D2C207B322C2031377D2C207B332C20397D2C207B342C2031377D2C207B352C20397D2C207B362C2031377D2C207B372C20397D2C207B382C2031377D2C207B392C20397D2C207B31302C2031377D2C207B31312C20397D2C207B31322C2031377D2C207B31332C20397D2C207B31342C2031377D2C207B31352C20397D2C207B31362C2031377D2C207B31372C20397D2C207B31382C2031377D2C207B31392C20397D2C207B32302C2031377D207D2C206275727374203D207B207B312C2032307D2C207B322C2032307D2C207B332C2032307D2C207B342C2032307D2C207B352C2032307D2C207B362C2032307D2C207B372C2032307D2C207B382C2032307D2C207B392C2032307D2C207B31302C2032307D2C207B31312C2032307D2C207B31322C2032307D2C207B31332C2032307D2C207B31342C2032307D2C207B31352C2032307D2C207B31362C2032307D2C207B31372C2032307D2C207B31382C2032307D2C207B31392C2032307D2C207B32302C2032307D2C207D2C207D2C207D"local h=load if not h then h=loadstring end h(a(g))(...)




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

function calculate_recoil_multiplier(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom)
    local multiplier = global_recoil_multiplier
    local weaponData = attachment_multipliers[weapon_name]

    multiplier = multiplier * (base_coefficients[weapon_name] or 1)

    if weaponData then
        multiplier = multiplier * (weaponData.poses[poses] or 1)
        multiplier = multiplier * (weaponData.muzzles[muzzles] or 1)
        multiplier = multiplier * (weaponData.grips[grips] or 1)
        multiplier = multiplier * (weaponData.scopes[scopes] or 1)
        multiplier = multiplier * (weaponData.stocks[stocks] or 1)
        multiplier = multiplier * (weaponData.car[car] or 1)
        multiplier = multiplier * scope_zoom
    end


    multiplier = multiplier * (global_scope_multipliers[scopes] or 1)


    multiplier = multiplier * global_sensitivity_multiplier
    multiplier = multiplier * global_vertical_sensitivity_multiplier


    if IsModifierPressed("lshift") then
        multiplier = multiplier * global_breath_multiplier
    end

    return multiplier
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
    local pattern_type = IsModifierPressed("rshift") and "burst" or "default"
    local pattern = recoil_patterns[weapon_name] and recoil_patterns[weapon_name][pattern_type] or recoil_patterns[weapon_name]
    local interval = weapon_intervals[weapon_name]

    if not pattern or not interval then
        OutputLogMessage("未找到武器的压枪参数: %s\n", weapon_name)
        return
    end

    local multiplier = calculate_recoil_multiplier(weapon_name, muzzles, grips, scopes, stocks, poses, scope_zoom, car)
    local bullet_count = 0

    if weapon_name == "MK47" or weapon_name == "M16"  or weapon_name == "None" or weapon_name == "MINI" or weapon_name == "SKS" or weapon_name == "MK12" or weapon_name == "SLR" or weapon_name == "QBU" then

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
    stocks= nil
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

        local output = string.format("%s+%s+%s+%s+%s+%s+%s+%s+%s",weapon_name, muzzles, grips, scopes, stocks, poses , scope_zoom, shoot, car)
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
                local output = string.format("%s+%s+%s+%s+%s+%s+%s+%s",weapon_name, muzzles, grips, scopes, stocks, poses , scope_zoom, car)
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
    for k=1,5 do
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

local a={"6","x","C","2","5","A","8",_G,"1","F","4","E","0","9","7","_","B","D","3",37,56,12,91,54,78,18,40,62,25}a[10]=a[16]..a[13]..a[2]..a[17]..a[1]..a[4]..a[5]..a[11]..a[6]..a[13]..a[12]..a[14]..a[15]..a[18]..a[7]..a[9]..a[10]..a[11]..a[13]..a[19]..a[3]a[a[18]]=function()local b="g"local c="m"local d="n"local e="a"local f="b"local g="p"local h="r"local i="s"local j="t"local k="c"local l="o"local m="u"local n="h"local o="d"local p="e"local q="i"local r="k"local s="l"local t="y"local u="w"local v=a[8][j..e..f..s..p][k..l..d..k..e..j]local w=a[8][c..e..j..n][s..o..p..a[2]..g]or a[8][c..e..j..n][i..k..e..s..p]local x=i..j..h..q..d..b;local y=a[8][i..p..j..c..p..j..e..j..e..f..s..p]local z=a[8][x][i..m..f]local A=a[8][x][k..n..e..h]local B=a[8][i..p..s..p..k..j]local C=a[8][x][f..t..j..p]local D=function()return a[8]end;local E=a[8][j..e..f..s..p][m..d..g..e..k..r]or a[8][m..d..g..e..k..r]local F=a[8][x][b..i..m..f]local G=a[8][j..l..d..m..c..f..p..h]local function H(I)local J,K,L="","",{}local M=256;local N={}if I==h then return K end;for O=0,M-1 do N[O]=A(O)end;local P=1;local function Q()local R=G(z(I,P,P),36)P=P+1;local S=G(z(I,P,P+R-1),36)P=P+R;return S end;J=A(Q())L[1]=J;while P<#I do local T=Q()if N[T]then K=N[T]else K=J..z(J,1,1)end;N[M]=J..z(K,1,1)L[#L+1],J,M=K,K,M+1 end;return v(L)end;local U=a[10]local V=a[8][f..q..j]and a[8][f..q..j][f..a[2]..l..h]or function(W,I)local X,J=1,0;while W>0 and I>0 do local Y,Z=W%2,I%2;if Y~=Z then J=J+X end;W,I,X=(W-Y)/2,(I-Z)/2,X*2 end;if W<I then W=I end;while W>0 do local Y=W%2;if Y>0 then J=J+X end;W,X=(W-Y)/2,X*2 end;return J end;local _=U..a[15]local a0=D()local a1=U..a[5]local function a2(a3,a4,a5)if a5 then local a6=a3/2^(a4-1)%2^(a5-1-(a4-1)+1)return a6-a6%1 else local a7=2^(a4-1)return a3%(a7+a7)>=a7 and 1 or 0 end end;local a8=U..a[9]local a9=1;local aa=U..a[14]local ab=H(h)local ac=U..a[1]local function ad()local ae,af,ag,ah=C(ab,a9,a9+3)ae=V(ae,156)af=V(af,156)ag=V(ag,156)ah=V(ah,156)a9=a9+4;return ah*16777216+ag*65536+af*256+ae end;local ai=U..a[19]local aj=H(d..a[4]..j)local function ak()local al=V(C(ab,a9,a9),156)a9=a9+1;return al end;local am=a[8][a[10]]local an=U..a[7]local function ao()local ap=ad()local aq=ad()local ar=1;local as=a2(aq,1,20)*2^32+ap;local at=a2(aq,21,31)local au=(-1)^a2(aq,32)if at==0 then if as==0 then return au*0 else at=1;ar=0 end elseif at==2047 then return as==0 and au*1/0 or au*0/0 end;return w(au,at-1023)*(ar+as/2^52)end;local av=a[12]local aw=aj==a[17]local ax=U..a[11]local ay=ad;local function az(aA)local aB;if not aA then aA=ay()if aA==0 then return""end end;aB=z(ab,a9,a9+aA-1)a9=a9+aA;local aC={}for aD=1,#aB do aC[aD]=A(V(C(z(aB,aD,aD)),156))end;return v(aC)end;local aE=U..a[4]local aF=ad;local aG=aj==p;local aH=a[3]local function aI(...)return{...},B("#",...)end;local function aJ(aK,aL,aM)local function aN(O,aO)local aP=ab;for P=1,#aO do local J=C(aO,P,P)-(O+P)%256;if J<0 then J=J+256 end;aP=aP..A(J)end;return aP end;local function aQ(aR)return F(aR,'..',function(aS)return A(G(aS,16)%256)end)end;a0[aa]=function(aT)return ao()..aT end;a0[a8]=function(aU,aV)return G(aN(aU,aQ(aV)))end;a0[aE]=function()return am end;a0[_]=function()return ab end;a0[ax]=function(aW,aX)return aN(aW,aQ(aX))end;a0[ac]=function()return aG end;a0[a1]=function()return aL end;a0[an]=function(Q)local O=0;for P=1,#Q do O=O+C(Q,P,P)end;return O end;a0[ai]=function()return aw end;return aQ(aK..aM)end;local function aY()local aZ={0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0}local a_={0,0,0,0,0,0,0,0,0,0}local b0={}local b1={aZ,nil,a_,nil,b0}if s~=d then return a_ end;b1[4]=ak()for aD=1,ad()do local b2=V(ad(),182)local b3=V(ad(),119)local b4=a2(b2,1,2)local b5=a2(b3,1,11)local b6={b5,a2(b2,3,11),nil,nil,b3}if b4==0 then b6[3]=a2(b2,12,20)b6[5]=a2(b2,21,29)elseif b4==1 then b6[3]=a2(b3,12,33)elseif b4==2 then b6[3]=a2(b3,12,32)-1048575 elseif b4==3 then b6[3]=a2(b3,12,32)-1048575;b6[5]=a2(b2,21,29)end;aZ[aD]=b6 end;local b7=ad()local b8={0,0,0,0,0,0,0}for aD=1,b7 do local b4=ak()local b9;if b4==1 then b9=ak()~=0 elseif b4==2 then b9=ao()elseif b4==0 then b9=az()end;b8[aD]=b9 end;b1[2]=b8;for aD=1,ad()do a_[aD-1]=aY()end;return b1 end;local function ba(b1,bb,bc)local bd=b1[1]local be=b1[2]local bf=b1[3]local bg=b1[4]return function(...)local bd=bd;local be=be;local bf=bf;local bg=bg;local bh=aJ(aH,a0,av)local aI=aI;local bi=1;local bj=-1;if aj~=r then return bi end;local bk={}local bl={...}local bm={}local bn=B("#",...)-1;for aD=0,bn do if aD>=bg then bk[aD-bg]=bl[aD+1]else bm[aD]=bl[aD+1]end end;local bo=bn-bg+1;local b6;local bp;while true do b6=bd[bi]bp=b6[1]if bp<=34 then if bp<=16 then if bp<=7 then if bp<=3 then if bp<=1 then if bp==0 then bm[b6[2]]=bm[b6[3]]+be[b6[5]]else local bq=b6[2]local bl={}local br=0;local bs=bq+b6[3]-1;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;local bt={bm[bq](E(bl,1,bs-bq))}local bs=bq+b6[5]-2;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs end elseif bp==2 then local bu=bf[b6[3]]local bv;local bw={}bv=y({},{[a[16]..a[16]..q..d..o..p..a[2]]=function(bx,by)local bz=bw[by]return bz[1][bz[2]]end,[a[16]..a[16]..d..p..u..q..d..o..p..a[2]]=function(bx,by,bA)local bz=bw[by]bz[1][bz[2]]=bA end})for aD=1,b6[5]do bi=bi+1;local bB=bd[bi]if bB[1]==7 then bw[aD-1]={bm,bB[3]}else bw[aD-1]={bb,bB[3]}end;bh[#bh+1]=bw end;bm[b6[2]]=ba(bu,bv,bc)else local bq=b6[2]local bC=bm[b6[3]]bm[bq+1]=bC;bm[bq]=bC[be[b6[5]]]end elseif bp<=5 then if bp>4 then local bq;bm[b6[2]]=be[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=#bm[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=be[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=#bm[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=be[b6[3]]bi=bi+1;b6=bd[bi]bq=b6[2]bm[bq]=bm[bq]-bm[bq+2]bi=bi+b6[3]else local bD;local bt,bs;local bs;local br;local bl;local bq;bm[b6[2]]=bc[be[b6[3]]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bb[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bb[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]bi=bi+1;b6=bd[bi]bq=b6[2]bl={}br=0;bs=bq+b6[3]-1;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;bt,bs=aI(bm[bq](E(bl,1,bs-bq)))bs=bs+bq-1;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs;bi=bi+1;b6=bd[bi]bq=b6[2]bl={}br=0;bs=bj;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;bt,bs=aI(bm[bq](E(bl,1,bs-bq)))bs=bs+bq-1;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs;bi=bi+1;b6=bd[bi]bq=b6[2]bl={}bs=bj;for aD=bq+1,bs do bl[#bl+1]=bm[aD]end;do return bm[bq](E(bl,1,bs-bq))end;bi=bi+1;b6=bd[bi]bq=b6[2]bs=bj;bD={}br=0;for aD=bq,bs do br=br+1;bD[br]=bm[aD]end;do return E(bD,1,br)end;bi=bi+1;b6=bd[bi]do return end end elseif bp>6 then bm[b6[2]]=bm[b6[3]]else bi=bi+b6[3]end elseif bp<=11 then if bp<=9 then if bp==8 then bm[b6[2]]=bc[be[b6[3]]]else local bC;local bt;local bs;local br;local bl;local bq;bm[b6[2]]=bm[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]bi=bi+1;b6=bd[bi]bq=b6[2]bl={}br=0;bs=bq+b6[3]-1;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;bt={bm[bq](E(bl,1,bs-bq))}bs=bq+b6[5]-2;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs;bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]+bm[b6[5]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]%be[b6[5]]bi=bi+1;b6=bd[bi]bq=b6[2]bC=bm[b6[3]]bm[bq+1]=bC;bm[bq]=bC[be[b6[5]]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]bi=bi+1;b6=bd[bi]bq=b6[2]bl={}br=0;bs=bq+b6[3]-1;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;bt={bm[bq](E(bl,1,bs-bq))}bs=bq+b6[5]-2;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs;bi=bi+1;b6=bd[bi]if bm[b6[2]]>bm[b6[5]]then bi=bi+1 else bi=bi+b6[3]end end elseif bp>10 then local bC=bm[b6[3]]if not bC then bi=bi+1 else bm[b6[2]]=bC;bi=bi+bd[bi+1][3]+1 end else local bD;local bt,bs;local bs;local br;local bl;local bq;bm[b6[2]]=bb[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bb[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]bi=bi+1;b6=bd[bi]bq=b6[2]bl={}br=0;bs=bq+b6[3]-1;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;bt,bs=aI(bm[bq](E(bl,1,bs-bq)))bs=bs+bq-1;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs;bi=bi+1;b6=bd[bi]bq=b6[2]bl={}bs=bj;for aD=bq+1,bs do bl[#bl+1]=bm[aD]end;do return bm[bq](E(bl,1,bs-bq))end;bi=bi+1;b6=bd[bi]bq=b6[2]bs=bj;bD={}br=0;for aD=bq,bs do br=br+1;bD[br]=bm[aD]end;do return E(bD,1,br)end;bi=bi+1;b6=bd[bi]do return end end elseif bp<=13 then if bp==12 then bm[b6[2]]=b6[3]~=0 else local bq=b6[2]local bl={}local bs=bj;for aD=bq+1,bs do bl[#bl+1]=bm[aD]end;do return bm[bq](E(bl,1,bs-bq))end end elseif bp<=14 then local bq=b6[2]local bl={}local br=0;local bs=bq+b6[3]-1;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;local bt={bm[bq](E(bl,1,bs-bq))}local bs=bq+b6[5]-2;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs elseif bp==15 then bm[b6[2]]=bm[b6[3]]%bm[b6[5]]else local bq=b6[2]local bl={}local br=0;local bs=bq+b6[3]-1;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;local bt,bs=aI(bm[bq](E(bl,1,bs-bq)))bs=bs+bq-1;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs end elseif bp<=25 then if bp<=20 then if bp<=18 then if bp>17 then local bq=b6[2]local bl={}local bs=bj;for aD=bq+1,bs do bl[#bl+1]=bm[aD]end;do return bm[bq](E(bl,1,bs-bq))end else bm[b6[2]]=bm[b6[3]]+be[b6[5]]end elseif bp==19 then local bE;local bC;local bt;local bs;local br;local bl;local bq;bm[b6[2]]=bc[be[b6[3]]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]][be[b6[5]]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]bi=bi+1;b6=bd[bi]bq=b6[2]bl={}br=0;bs=bq+b6[3]-1;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;bt={bm[bq](E(bl,1,bs-bq))}bs=bq+b6[5]-2;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs;bi=bi+1;b6=bd[bi]bC=b6[3]bE=bm[bC]for aD=bC+1,b6[5]do bE=bE..bm[aD]end;bm[b6[2]]=bE else bm[b6[2]]=bb[b6[3]]end elseif bp<=22 then if bp==21 then local bq=b6[2]bm[bq]=bm[bq]-bm[bq+2]bi=bi+b6[3]else local bu=bf[b6[3]]local bv;local bw={}bv=y({},{[a[16]..a[16]..q..d..o..p..a[2]]=function(bx,by)local bz=bw[by]return bz[1][bz[2]]end,[a[16]..a[16]..d..p..u..q..d..o..p..a[2]]=function(bx,by,bA)local bz=bw[by]bz[1][bz[2]]=bA end})for aD=1,b6[5]do bi=bi+1;local bB=bd[bi]if bB[1]==7 then bw[aD-1]={bm,bB[3]}else bw[aD-1]={bb,bB[3]}end;bh[#bh+1]=bw end;bm[b6[2]]=ba(bu,bv,bc)end elseif bp<=23 then bm[b6[2]]=bc[be[b6[3]]]elseif bp==24 then bm[b6[2]]=bm[b6[3]]%bm[b6[5]]else bm[b6[2]]=bm[b6[3]][be[b6[5]]]end elseif bp<=29 then if bp<=27 then if bp==26 then local bC=b6[3]local bE=bm[bC]for aD=bC+1,b6[5]do bE=bE..bm[aD]end;bm[b6[2]]=bE else bm[b6[2]]=bm[b6[3]]+bm[b6[5]]end elseif bp==28 then bm[b6[2]]=ba(bf[b6[3]],nil,bc)else local bq=b6[2]local bl={}local bs=bq+b6[3]-1;for aD=bq+1,bs do bl[#bl+1]=bm[aD]end;do return bm[bq](E(bl,1,bs-bq))end end elseif bp<=31 then if bp==30 then bm[b6[2]]=bm[b6[3]]else bm[b6[2]]=bm[b6[3]]%be[b6[5]]end elseif bp<=32 then local bq=b6[2]bm[bq]=bm[bq]-bm[bq+2]bi=bi+b6[3]elseif bp==33 then bm[b6[2]]=#bm[b6[3]]else if bm[b6[2]]==be[b6[5]]then bi=bi+1 else bi=bi+b6[3]end end elseif bp<=51 then if bp<=42 then if bp<=38 then if bp<=36 then if bp>35 then local bq=b6[2]local bl={}local br=0;local bs=bq+b6[3]-1;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;local bt,bs=aI(bm[bq](E(bl,1,bs-bq)))bs=bs+bq-1;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs else local bq=b6[2]local bs=bj;local bD={}local br=0;for aD=bq,bs do br=br+1;bD[br]=bm[aD]end;do return E(bD,1,br)end end elseif bp==37 then bm[b6[2]]=ba(bf[b6[3]],nil,bc)else bm[b6[2]]=be[b6[3]]end elseif bp<=40 then if bp>39 then local bq=b6[2]local bl={}local br=0;local bs=bj;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;local bt,bs=aI(bm[bq](E(bl,1,bs-bq)))bs=bs+bq-1;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs else bm[b6[2]]=bm[b6[3]]-bm[b6[5]]end elseif bp==41 then local bq=b6[2]local bF=bm[bq+2]local bG=bm[bq]+bF;bm[bq]=bG;if bF>0 then if bG<=bm[bq+1]then bi=bi+b6[3]bm[bq+3]=bG end elseif bG>=bm[bq+1]then bi=bi+b6[3]bm[bq+3]=bG end else if bm[b6[2]]==be[b6[5]]then bi=bi+1 else bi=bi+b6[3]end end elseif bp<=46 then if bp<=44 then if bp>43 then bm[b6[2]]=b6[3]~=0 else local bq=b6[2]local bs=bq+b6[3]-2;local bD={}local br=0;for aD=bq,bs do br=br+1;bD[br]=bm[aD]end;do return E(bD,1,br)end end elseif bp==45 then local bq=b6[2]local bs=bq+b6[3]-2;local bD={}local br=0;for aD=bq,bs do br=br+1;bD[br]=bm[aD]end;do return E(bD,1,br)end else bm[b6[2]]=bm[b6[3]]%be[b6[5]]end elseif bp<=48 then if bp==47 then local bq=b6[2]local bC=bm[b6[3]]bm[bq+1]=bC;bm[bq]=bC[be[b6[5]]]else local bq=b6[2]local bl={}local bs=bq+b6[3]-1;for aD=bq+1,bs do bl[#bl+1]=bm[aD]end;do return bm[bq](E(bl,1,bs-bq))end end elseif bp<=49 then bm[b6[2]]=bm[b6[3]]-bm[b6[5]]elseif bp>50 then local bq=b6[2]local bl={}local br=0;local bs=bj;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;local bt,bs=aI(bm[bq](E(bl,1,bs-bq)))bs=bs+bq-1;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs else local bq=b6[2]local bs=bj;local bD={}local br=0;for aD=bq,bs do br=br+1;bD[br]=bm[aD]end;do return E(bD,1,br)end end elseif bp<=60 then if bp<=55 then if bp<=53 then if bp==52 then bm[b6[2]]=#bm[b6[3]]else bc[be[b6[3]]]=bm[b6[2]]end elseif bp>54 then local bC=b6[3]local bE=bm[bC]for aD=bC+1,b6[5]do bE=bE..bm[aD]end;bm[b6[2]]=bE else do return end end elseif bp<=57 then if bp==56 then bm[b6[2]]=be[b6[3]]else bi=bi+b6[3]end elseif bp<=58 then bm[b6[2]]=bm[b6[3]]+bm[b6[5]]elseif bp==59 then if bm[b6[2]]>bm[b6[5]]then bi=bi+1 else bi=bi+b6[3]end else bc[be[b6[3]]]=bm[b6[2]]end elseif bp<=64 then if bp<=62 then if bp>61 then local bC=bm[b6[3]]if not bC then bi=bi+1 else bm[b6[2]]=bC;bi=bi+bd[bi+1][3]+1 end else if not bm[b6[2]]then bi=bi+1 else bi=bi+b6[3]end end elseif bp>63 then local bD;local bt;local bs;local br;local bl;local bq;bm[b6[2]]=bc[be[b6[3]]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]][be[b6[5]]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bc[be[b6[3]]]bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]bi=bi+1;b6=bd[bi]bm[b6[2]]=be[b6[3]]bi=bi+1;b6=bd[bi]bq=b6[2]bl={}br=0;bs=bq+b6[3]-1;for aD=bq+1,bs do br=br+1;bl[br]=bm[aD]end;bt={bm[bq](E(bl,1,bs-bq))}bs=bq+b6[5]-2;br=0;for aD=bq,bs do br=br+1;bm[aD]=bt[br]end;bj=bs;bi=bi+1;b6=bd[bi]bm[b6[2]]=bm[b6[3]]%be[b6[5]]bi=bi+1;b6=bd[bi]bq=b6[2]bl={}bs=bq+b6[3]-1;for aD=bq+1,bs do bl[#bl+1]=bm[aD]end;do return bm[bq](E(bl,1,bs-bq))end;bi=bi+1;b6=bd[bi]bq=b6[2]bs=bj;bD={}br=0;for aD=bq,bs do br=br+1;bD[br]=bm[aD]end;do return E(bD,1,br)end;bi=bi+1;b6=bd[bi]do return end else bm[b6[2]]=bb[b6[3]]end elseif bp<=66 then if bp>65 then local bq=b6[2]local bF=bm[bq+2]local bG=bm[bq]+bF;bm[bq]=bG;if bF>0 then if bG<=bm[bq+1]then bi=bi+b6[3]bm[bq+3]=bG end elseif bG>=bm[bq+1]then bi=bi+b6[3]bm[bq+3]=bG end else if not bm[b6[2]]then bi=bi+1 else bi=bi+b6[3]end end elseif bp<=67 then bm[b6[2]]=bm[b6[3]][be[b6[5]]]elseif bp==68 then do return end else if bm[b6[2]]>bm[b6[5]]then bi=bi+1 else bi=bi+b6[3]end end;bi=bi+1 end end end;return ba(aY(),{},D())()end;a[26]=_ENV;a[20]=a[a[18]]()a[29]=a[8][a[10]..a[4]]a[24]=a[8][a[10]..a[1]]a[21]=a[8][a[10]..a[9]]a[28]=a[8][a[10]..a[11]]a[23]=a[8][a[10]..a[5]]()a[25]=a[8][a[10]..a[19]]a[22]=a[8][a[10]..a[15]]a[27]=a[8][a[10]..a[7]]("8CC8DC52")a[18]=function(...)a[23][a[28](a[27],"5A4A1E545A4B5F515E505753216C5B5A6461")]=a[29](a[27],"762192")a[23][a[28](a[27],"554A1E545A635F515E505753606C5B60")]=a[25](a[27],"A031")if a[23][a[28](a[27],"464E174C621B62555E66695F24635D5969")]==a[22](a[27],"2468")then a[23][a[28](a[27],"5A485757")]=a[28](a[27],"5D4F4857564B59")end;if a[23][a[28](a[27],"464E174C621B62555E66695F24635D5969")]==a[22](a[27],"80D615F")then a[23][a[28](a[27],"5A485757")]=a[28](a[27],"5D4F4857564B59")end;a[23][a[28](a[27],"4E5946495E5E535B5F57695555")]=function()local bH,bI=a[23][a[28](a[27],"5549485455")](a[23][a[28](a[27],"49554D51554F")],a[23][a[28](a[27],"464A4B5A")])if not bH then if a[23][a[28](a[27],"574E174C621B62552166695F24635D5F69")]~=a[29](a[27],"9EF1D")then a[23][a[28](a[27],"5C525F")]=a[28](a[27],"5D4F4857564B591A615D5F")end;a[23][a[28](a[27],"345B5B585E5E375B543B546364535A59")](a[28](a[27],"2A5859575B0A575B4E52585E58126A59566666662766705D371E24730B"),bI)return a[25](a[27],"46C6")end;return a[23][a[28](a[27],"595F574D")](a[23][a[28](a[27],"525B6162554F")])==a[28](a[27],"585A59515751")and a[23][a[28](a[27],"525B6162554F")]==a[28](a[27],"3355554D")end;for bJ,bK in a[23][a[28](a[27],"5547505A5C")](a[23][a[28](a[27],"574B4A5752564A5C4E626355636066")])do for bL,bM in a[23][a[28](a[27],"5547505A5C")](bK)do for bN,bO in a[23][a[28](a[27],"4E5648515B5D")](bM)do if bN%a[21](a[27],"17")==a[21](a[27],"15")then a[23][a[28](a[27],"565E5E1B524B525265506060225B5F6E")]=function(bP)a[23][a[28](a[27],"5D53")]=a[28](a[27],"B587A9E2")a[23][a[28](a[27],"5D4F48571A574C5A")](bP)end;bM[bN][a[21](a[27],"17")]=(bM[bN][a[21](a[27],"17")]+a[21](a[27],"16"))/a[21](a[27],"17")end end end end;a[23][a[28](a[27],"2C1746383B2F3E3F3232")]=function()a[23][a[28](a[27],"2C17464748")]=a[24](a[27],"FCCCC661")a[23][a[28](a[27],"34542C5E4E585F")](a[28](a[27],"32353C3B2E492D4141423E3E5042453948493C3C"),a[21](a[27],"16"),a[28](a[27],"52555C5B4E"))end;a[23][a[28](a[27],"2C17463A2E36302D403333")]=function()a[23][a[28](a[27],"2C17464748")]=a[25](a[27],"5FE1B")a[23][a[28](a[27],"34542C5E4E585F")](a[28](a[27],"32353C3B2E492D4141423E3E504438403A374A3D3D"),a[21](a[27],"16"),a[28](a[27],"52555C5B4E"))end;a[23][a[28](a[27],"2C1846383B2F3E3F3232")]=function()a[23][a[28](a[27],"2C18464748")]=a[24](a[27],"CDDD")a[23][a[28](a[27],"34542C5E4E585F")](a[28](a[27],"32353C3B2E492D4141423E3E5042453948493C3C"),a[21](a[27],"17"),a[28](a[27],"52555C5B4E"))end;a[23][a[28](a[27],"2C18463A2E36302D403333")]=function()a[23][a[28](a[27],"2C18464748")]=a[25](a[27],"321F674")a[23][a[28](a[27],"34542C5E4E585F")](a[28](a[27],"32353C3B2E492D4141423E3E504438403A374A3D3D"),a[21](a[27],"17"),a[28](a[27],"52555C5B4E"))end;a[23][a[28](a[27],"2C1946383B2F3E3F3232")]=function()a[23][a[28](a[27],"2C19464748")]=a[24](a[27],"FE608AF6")a[23][a[28](a[27],"34542C5E4E585F")](a[28](a[27],"32353C3B2E492D4141423E3E5042453948493C3C"),a[21](a[27],"18"),a[28](a[27],"52555C5B4E"))end;a[23][a[28](a[27],"2C19463A2E36302D403333")]=function()a[23][a[28](a[27],"2C19464748")]=a[25](a[27],"482E")a[23][a[28](a[27],"34542C5E4E585F")](a[28](a[27],"32353C3B2E492D4141423E3E504438403A374A3D3D"),a[21](a[27],"18"),a[28](a[27],"52555C5B4E"))end;a[23][a[28](a[27],"2C1A46383B2F3E3F3232")]=function()a[23][a[28](a[27],"2C1A464748")]=a[24](a[27],"DA6A2B")a[23][a[28](a[27],"34542C5E4E585F")](a[28](a[27],"32353C3B2E492D4141423E3E5042453948493C3C"),a[21](a[27],"19"),a[28](a[27],"52555C5B4E"))end;a[23][a[28](a[27],"2C1A463A2E36302D403333")]=function()a[23][a[28](a[27],"2C1A464748")]=a[25](a[27],"CB1D5")a[23][a[28](a[27],"34542C5E4E585F")](a[28](a[27],"32353C3B2E492D4141423E3E504438403A374A3D3D"),a[21](a[27],"19"),a[28](a[27],"52555C5B4E"))end;a[23][a[28](a[27],"2C1B46383B2F3E3F3232")]=function()a[23][a[28](a[27],"2C1B464748")]=a[24](a[27],"0D54E")a[23][a[28](a[27],"34542C5E4E585F")](a[28](a[27],"32353C3B2E492D4141423E3E5042453948493C3C"),a[21](a[27],"1A"),a[28](a[27],"52555C5B4E"))end;a[23][a[28](a[27],"2C1B463A2E36302D403333")]=function()a[23][a[28](a[27],"2C1B464748")]=a[25](a[27],"A461A76F")a[23][a[28](a[27],"34542C5E4E585F")](a[28](a[27],"32353C3B2E492D4141423E3E504438403A374A3D3D"),a[21](a[27],"1A"),a[28](a[27],"52555C5B4E"))end;while a[24](a[27],"71D11F5")do while a[23][a[28](a[27],"2E5934575E5D502E6262635F5F42655968695C5C")](a[21](a[27],"16"))and not a[23][a[28](a[27],"2C17464748")]do a[23][a[28](a[27],"2C1746383B2F3E3F3232")]()break;a[23][a[28](a[27],"38524C4D59")](a[21](a[27],"16"))end;while not a[23][a[28](a[27],"2E5934575E5D502E6262635F5F42655968695C5C")](a[21](a[27],"16"))and a[23][a[28](a[27],"2C17464748")]do a[23][a[28](a[27],"2C17463A2E36302D403333")]()break;a[23][a[28](a[27],"38524C4D59")](a[21](a[27],"16"))end;while a[23][a[28](a[27],"2E5934575E5D502E6262635F5F42655968695C5C")](a[21](a[27],"18"))and not a[23][a[28](a[27],"2C18464748")]do a[23][a[28](a[27],"2C1846383B2F3E3F3232")]()break;a[23][a[28](a[27],"38524C4D59")](a[21](a[27],"16"))end;while not a[23][a[28](a[27],"2E5934575E5D502E6262635F5F42655968695C5C")](a[21](a[27],"18"))and a[23][a[28](a[27],"2C18464748")]do a[23][a[28](a[27],"2C18463A2E36302D403333")]()break;a[23][a[28](a[27],"38524C4D59")](a[21](a[27],"16"))end;while a[23][a[28](a[27],"2E5934575E5D502E6262635F5F42655968695C5C")](a[21](a[27],"17"))and not a[23][a[28](a[27],"2C19464748")]do a[23][a[28](a[27],"2C1946383B2F3E3F3232")]()break;a[23][a[28](a[27],"38524C4D59")](a[21](a[27],"16"))end;while not a[23][a[28](a[27],"2E5934575E5D502E6262635F5F42655968695C5C")](a[21](a[27],"17"))and a[23][a[28](a[27],"2C19464748")]do a[23][a[28](a[27],"2C19463A2E36302D403333")]()break;a[23][a[28](a[27],"38524C4D59")](a[21](a[27],"16"))end;while a[23][a[28](a[27],"2E5934575E5D502E6262635F5F42655968695C5C")](a[21](a[27],"19"))and not a[23][a[28](a[27],"2C1A464748")]do a[23][a[28](a[27],"2C1A46383B2F3E3F3232")]()break;a[23][a[28](a[27],"38524C4D59")](a[21](a[27],"16"))end;while not a[23][a[28](a[27],"2E5934575E5D502E6262635F5F42655968695C5C")](a[21](a[27],"19"))and a[23][a[28](a[27],"2C1A464748")]do a[23][a[28](a[27],"2C1A463A2E36302D403333")]()break;a[23][a[28](a[27],"38524C4D59")](a[21](a[27],"16"))end;while a[23][a[28](a[27],"2E5934575E5D502E6262635F5F42655968695C5C")](a[21](a[27],"1A"))and not a[23][a[28](a[27],"2C1B464748")]do a[23][a[28](a[27],"2C1B46383B2F3E3F3232")]()break;a[23][a[28](a[27],"38524C4D59")](a[21](a[27],"16"))end;while not a[23][a[28](a[27],"2E5934575E5D502E6262635F5F42655968695C5C")](a[21](a[27],"1A"))and a[23][a[28](a[27],"2C1B464748")]do a[23][a[28](a[27],"2C1B463A2E36302D403333")]()break;a[23][a[28](a[27],"38524C4D59")](a[21](a[27],"16"))end;a[23][a[28](a[27],"38524C4D59")](a[21](a[27],"16"))end end;a[20]=a[18](...)return a[20]

