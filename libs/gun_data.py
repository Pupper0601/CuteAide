#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : Pupper
# @Email  : pupper.cheng@gmail.com


global_recoil = 1   # 全局后坐力

alone_factor = {    # 单独武器基础影响因子
     "AKM": 1.0,
     "M762": 1.0,
     "G36C": 1.0,
     "M416": 1.0,
     "M16A4": 1.0,
     "SCARL": 1.0,
     "MK47": 1.0,
     "QBZ": 1.0,
     "AUG": 1.0,
     "GROZA": 1.0,
     "ACE32": 1.0,
     "K2": 1.0,
     "FAMAS": 1.0,
     "ZDZT": 1.0,
     "MINI14": 1.0,
     "SKS": 1.0,
     "VSS": 1.0,
     "QBU": 1.0,
     "MK14": 1.0,
     "MK12": 1.0,
     "DLGNF": 1.0,
     "PP19": 1.0,
     "TMX": 1.0,
     "UMP": 1.0,
     "UZI": 1.0,
     "VECTOR": 1.0,
     "MP5K": 1.0,
     "P90": 1.0,
     "JS9": 1.0,
     "MP9": 1.0,
     "DP28": 1.0,
     "M249": 1.0,
     "MG3": 1.0
}

component_factor = {    # 配件影响因子
    "weapon_none": {
        "poses":{       # 姿势
            "stand": 1, # 站
            "squat": 0.75,  # 蹲
            "crawl":0.5,    # 爬
        },
        "muzzles": {     # 枪口
            "xiaoyan-b": 0.86,
            "buchang-b": 0.78,
            "zhituiqi" :0.87,
        },
        "grips": {
            "zhijiao": 1,
            "banjie": 0.83,
            "qingxin": 0.78,
            "muzhi": 0.83,
        },
        "scopes": {
            "reddot": 0.55,
            "quanxi": 0.55,
            "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.45,
        },
        "stocks": {
            "zhanshu": 1,
            "zhongxing": 0.86,
            "zhedie": 0.86,
        },
        "car": {
            "car": 1.5,
        },
    },
    "AKM": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.75,
            "crawl": 0.47,
        },
        "muzzles": {
            "xiaoyan-b" : 0.85,
            "buchang-b" : 0.76,
            "zhituiqi"  : 0.86,
        },
        "scopes" : {
            "reddot": 0.55,
            "quanxi": 0.55,
            "x2"    : 1,
            "x3"    : 1.44,
            "x4"    : 2,
            "x6"    : 1.44,
        },
        "car"    : {
            "car" : 1.5,
        },
    },
    "M762": {
        "poses": {
            "stand": 1,
            "squat": 0.83,
            "crawl": 0.58,
        },
        "muzzles": {
            "xiaoyan-b": 0.85,
            "buchang-b": 0.79,
            "zhituiqi": 0.87,
        },
        "grips": {
            "zhijiao": 1,
            "banjie": 0.82,
            "qingxin": 0.78,
            "muzhi": 0.81,
            "jiguang": 0.87,
        },
        "scopes": {
            "reddot": 0.55,
            "quanxi": 0.55,
            "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.44,
        },
        "car": {
            "car": 1.5,
        },
    },
    "G36C": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.75,
            "crawl": 0.5,
        },
        "muzzles": {
            "xiaoyan-b" : 0.86,
            "buchang-b" : 0.78,
            "zhituiqi"  : 0.87,
        },
        "grips"  : {
            "zhijiao": 1,
            "banjie"  : 0.79,
            "qingxin" : 0.78,
            "muzhi": 0.76,
            "jiguang": 0.79,
        },
        "scopes" : {
            "reddot": 0.55,
            "quanxi": 0.55,
            "x2"    : 1,
            "x3"    : 1.44,
            "x4"    : 2,
            "x6"    : 1.45,
        },
        "car"    : {
            "car" : 1.5,
        },
    },
    "M416": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.75,
            "crawl": 0.5,
        },
        "muzzles": {
            "xiaoyan-b" : 0.86,
            "buchang-b" : 0.79,
            "zhituiqi"  : 0.88,
        },
        "grips"  : {
            "zhijiao": 1,
            "banjie"  : 0.83,
            "qingxin" : 0.78,
            "muzhi": 0.8,
            "jiguang": 0.88,
        },
        "scopes" : {
            "reddot": 0.55,
            "quanxi": 0.55,
            "x2"    : 1,
            "x3"    : 1.44,
            "x4"    : 2,
            "x6"    : 1.45,
        },
        "stocks" : {
            "zhanshu": 1,
            "zhongxing" : 0.86,
        },
        "car"    : {
            "car" : 1.5,
        },
    },
    "M16A4": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.78,
            "crawl": 0.5,
        },
        "muzzles": {
            "xiaoyan-b" : 0.83,
            "buchang-b" : 0.74,
            "zhituiqi"  : 0.84,
        },
        "scopes" : {
            "reddot": 1,
            "quanxi": 1,
            "x2"    : 1.8,
            "x3"    : 2.6,
            "x4"    : 3.6,
            "x6"    : 2.6,
        },
        "stocks" : {
            "zhanshu": 1,
            "zhongxing" : 0.86,
        },
        "car"    : {
            "car" : 1.5,
        },
    },
    "SCARL": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.75,
            "crawl": 0.5,
        },
        "muzzles": {
            "xiaoyan-b" : 0.86,
            "buchang-b" : 0.78,
            "zhituiqi"  : 0.87,
        },
        "grips"  : {
            "zhijiao": 1,
            "banjie"  : 0.84,
            "qingxin" : 0.78,
            "muzhi": 0.8,
            "jiguang": 0.82
        },
        "scopes" : {
            "reddot": 0.5,
            "quanxi": 0.5,
            "x2"    : 1,
            "x3"    : 1.44,
            "x4"    : 2,
            "x6"    : 1.45,
        },
        "car"    : {
            "car" : 1.5,
        },
    },
    "MK47": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.78,
            "crawl": 0.53,
        },
        "muzzles": {
            "xiaoyan-b" : 0.84,
            "buchang-b" : 0.75,
            "zhituiqi"  : 0.84,
        },
        "grips"  : {
            "zhijiao": 1,
            "banjie"  : 0.83,
            "qingxin" : 0.78,
            "muzhi": 0.83,
        },
        "scopes" : {
            "reddot": 1,
            "quanxi": 1,
            "x2"    : 1.8,
            "x3"    : 2.6,
            "x4"    : 3.6,
            "x6"    : 2.6,
        },
        "stocks" : {
            "zhanshu": 1,
            "zhongxing" : 0.86,
        },
        "car"    : {
            "car" : 1.5,
        },
    },
    "QBZ": {
        "poses"  : {
            "stand": 0.92,
            "squat" : 0.75,
            "crawl": 0.5,
        },
        "muzzles": {
            "xiaoyan-b" : 0.88,
            "buchang-b" : 0.8,
            "zhituiqi"  : 0.88,
        },
        "grips"  : {
            "zhijiao": 1,
            "banjie"  : 0.815,
            "qingxin" : 0.78,
            "muzhi": 0.83,
            "jiguang": 0.79,
        },
        "scopes" : {
            "reddot": 0.55,
            "quanxi": 0.55,
            "x2"    : 1,
            "x3"    : 1.44,
            "x4"    : 2,
            "x6"    : 1.45,
        },
        "car"    : {
            "car" : 1.5,
        },
    },
    "AUG": {
        "poses": {
            "stand": 1,
            "squat": 0.8,
            "crawl": 0.5,
        },
        "muzzles": {
            "xiaoyan-b": 0.84,
            "buchang-b": 0.78,
            "zhituiqi": 0.86,
        },
        "grips": {
            "zhijiao": 1,
            "banjie": 0.84,
            "qingxin": 0.78,
            "muzhi": 0.81,
        },
        "scopes": {
            "reddot": 0.55,
            "quanxi": 0.55,
            "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.44,
        },
        "car": {
            "car": 1.5,
        },
    },
    "GROZA": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.7,
            "crawl": 0.47,
        },
        "muzzles": {
            "xiaoyan-b" : 0.86,
            "buchang-b" : 0.78,
            "xx"  : 1,
            "zhituiqi"  : 0.87,
        },
        "scopes" : {
            "reddot": 0.55,
            "quanxi": 0.55,
            "x2"    : 1,
            "x3"    : 1.44,
            "x4"    : 2,
            "x6"    : 1.45,
        },
        "car"    : {
            "car" : 1.5,
        },
    },
    "ACE32": {
        "poses": {
            "stand": 1,
            "squat": 0.75,
            "crawl": 0.5,
        },
        "muzzles": {
            "xiaoyan-b": 0.86,
            "buchang-b": 0.78,
            "zhituiqi": 0.87,
        },
        "grips": {
            "zhijiao": 1,
            "banjie": 0.83,
            "qingxin": 0.78,
            "muzhi": 0.8,
            "jiguang": 0.86,
        },
        "scopes": {
            "reddot": 0.55,
            "quanxi": 0.55,
            "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.45,
        },
        "stocks": {
            "zhanshu": 1,
            "zhongxing": 0.86,
        },
        "car": {
            "car": 1.5,
        },
    },
    "K2": {
        "poses": {
            "stand": 1,
            "squat": 0.75,
            "crawl": 0.5,
        },
        "muzzles": {
            "xiaoyan-b": 0.86,
            "buchang-b": 0.78,
            "xx": 1,
            "zhituiqi": 0.87,
        },
        "scopes": {
            "reddot": 0.55,
            "quanxi": 0.55,
            "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.45,
        },
        "car": {
            "car": 1.5,
        },
    },
    "FAMAS": {
        "poses": {
            "stand": 1,
            "squat": 0.75,
            "crawl": 0.5,
        },
        "muzzles": {
            "xiaoyan-b": 0.86,
            "buchang-b": 0.8,
            "zhituiqi": 0.83,
        },
        "scopes": {
            "reddot": 0.55,
            "quanxi": 0.55,
            "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.45,
        },
        "car": {
            "car": 1.5,
        },
    },
    "ZDZT": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.77,
            "crawl": 0.5,
        },
        "muzzles": {
            "xiaoyan-b" : 0.94,
            "xiaoyan-j" : 0.94,
            "buchang-b" : 0.9,
            "buchang-j" : 0.9,
            "zhituiqi"  : 0.85,

        },
        "scopes" : {
            "reddot": 2.5,
            "quanxi": 2.5,
            "x2"    : 1,
            "x3"    : 1,
            "x4"    : 1.1,
            "x6"    : 0.9,
            "x8"    : 1,
        },
        "stocks" : {
            "tosaiban": 0.86,
        },
        "car"    : {
            "car" : 1.5,
        },

    },
    "MINI14": {
        "poses"  : {
            "stand": 1.05,
            "squat" : 0.72,
            "crawl": 1.05,
        },
        "muzzles": {
            "xiaoyan-b" : 0.94,
            "xiaoyan-j" : 0.94,
            "buchang-b" : 0.9,
            "buchang-j" : 0.9,
            "zhituiqi"  : 0.85,
        },
        "scopes" : {
            "reddot": 1.5,
            "quanxi": 1.5,
            "x2"    : 1,
            "x3"    : 1,
            "x4"    : 1.16,
            "x6"    : 1,
            "x8"    : 1.16,
        },
        "car"    : {
            "car" : 1.5,
        },

    },
    "SKS": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.75,
            "crawl": 1,
        },
        "muzzles": {
            "xiaoyan-b" : 0.94,
            "xiaoyan-j" : 0.94,
            "buchang-b" : 0.9,
            "buchang-j" : 0.9,
            "zhituiqi"  : 0.85,
        },
        "scopes" : {
            "reddot": 2.5,
            "quanxi": 2.5,
            "x2"    : 1,
            "x3"    : 1,
            "x4"    : 1.1,
            "x6"    : 1,
            "x8"    : 1.1,
        },
        "grips"  : {
            "zhijiao": 1,
            "banjie"  : 0.83,
            "qingxin" : 0.79,
            "muzhi": 0.83,
        },
        "stocks" : {
            "tosaiban" : 0.86,
        },
        "car"    : {
            "None": 1,
            "car" : 1.5,
        },

    },
    "VSS": {
        "poses"  : {
            "stand": 1,
            "squat" : 1,
            "crawl": 1,
        },
        "stocks" : {
            "tosaiban" : 0.86,
        },
        "car"    : {
            "car" : 1.5,
        },

    },
    "QBU": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.78,
            "crawl": 0.86,
        },
        "muzzles": {
            "xiaoyan-b" : 0.94,
            "xiaoyan-j" : 0.94,
            "buchang-b" : 0.9,
            "buchang-j" : 0.9,
            "zhituiqi"  : 0.85,
        },
        "scopes" : {
            "reddot": 1.5,
            "quanxi": 1.5,
            "x2"    : 1,
            "x3"    : 1,
            "x4"    : 1.1,
            "x6"    : 1,
            "x8"    : 1,
        },
        "car"    : {
            "car" : 1.5,
        },

    },
    "MK14": {
        "poses"  : {
            "stand": 0.95,
            "squat" : 0.77,
            "crawl": 0.7,
        },
        "muzzles": {
            "xiaoyan-b" : 0.94,
            "xiaoyan-j" : 0.94,
            "buchang-b" : 0.9,
            "buchang-j" : 0.9,
            "zhituiqi"  : 0.85,
        },
        "scopes" : {
            "reddot": 1,
            "quanxi": 1,
            "x2"    : 1,
            "x3"    : 1,
            "x4"    : 1.1,
            "x6"    : 1,
            "x8"    : 1.2,
        },
        "stocks" : {
            "tosaiban" : 0.86,
        },
        "car"    : {
            "car" : 1.5,
        },

    },
    "MK12": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.78,
            "crawl": 0.7,
        },

        "muzzles": {
            "xiaoyan-b" : 0.94,
            "xiaoyan-j" : 0.94,
            "buchang-b" : 0.9,
            "buchang-j" : 0.9,
            "zhituiqi"  : 0.85,
        },
        "scopes" : {
            "reddot": 1.5,
            "quanxi": 1.5,
            "x2"    : 1,
            "x3"    : 1,
            "x4"    : 1.1,
            "x6"    : 1,
            "x8"    : 1,
        },
        "grips"  : {
            "zhijiao": 1,
            "banjie"  : 0.83,
            "qingxin" : 0.79,
            "muzhi": 0.83,
        },
        "car"    : {
            "car" : 1.5,
        },

    },
    "DLGNF": {
        "poses"  : {
            "stand": 1.3,
            "squat" : 0.84,
            "crawl": 0.86,
        },
        "muzzles": {
            "xiaoyan-b" : 0.94,
            "xiaoyan-j" : 0.94,
            "buchang-b" : 0.9,
            "buchang-j" : 0.9,
            "zhituiqi"  : 0.85,
        },
        "scopes" : {
            "reddot": 2.5,
            "quanxi": 2.5,
            "x2"    : 1,
            "x3"    : 1,
            "x4"    : 1.3,
            "x6"    : 1,
            "x8"    : 1.4,
        },
        "stocks" : {
            "tosaiban" : 0.86,
        },
        "car"    : {
            "car" : 1.5,
        },

    },
    "PP19": {
        "poses": {
            "stand": 1,
            "squat": 0.77,
            "crawl": 0.7,
        },
        "muzzles": {
            "buchang-c": 0.8,
            "xiaoyan-c": 0.9,
        },
        "scopes": {
            "reddot": 0.51,
            "quanxi": 0.51,
            "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.45,
        },
        "car": {
            "car": 1.5,
        },
    },
    "TMX": {
        "poses": {
            "stand": 1,
            "squat": 0.7,
            "crawl": 0.62,
        },
        "grips": {
            "qingxin": 0.78	,
        },
        "scopes": {
            "reddot": 0.51,
            "quanxi": 0.51,
        },
        "car": {
            "car": 1.5,
        },
    },
    "UMP": {
        "poses": {
            "stand": 1,
            "squat": 0.74,
            "crawl": 0.7,
        },
        "muzzles": {
            "buchang-c": 0.8,
            "xiaoyan-c": 0.9,
        },
        "grips": {
            "zhijiao": 1,
            "banjie": 0.83,
            "qingxin": 0.79,
            "muzhi": 0.83,
            "jiguang": 0.83,
        },
        "scopes": {
            "reddot": 0.52,
            "quanxi": 0.52,
            "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.45,
        },
        "car": {
            "car": 1.5,
        },
    },
    "UZI": {
        "poses": {
            "stand": 1,
            "squat": 0.73,
            "crawl": 0.6,
        },
        "muzzles": {
            "buchang-c": 0.68,
            "xiaoyan-c": 0.88,
        },
        "scopes": {
            "reddot": 0.51,
            "quanxi": 0.51,
        },
        "stocks": {
            "zhedie": 1,
        },
        "car": {
            "car": 1.5,
        },
    },
    "VECTOR": {
        "poses": {
            "stand": 1,
            "squat": 0.75,
            "crawl": 0.64,
        },
        "muzzles": {
            "buchang-c": 0.8,
            "xiaoyan-c": 0.9,
        },
        "grips": {
            "banjie": 0.83,
            "qingxin": 0.79,
            "jiguang": 0.83,
        },
        "scopes": {
            "reddot": 0.52,
            "quanxi": 0.52,
            "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.45,
        },
        "stocks": {
            "zhongxing": 1,
            "zhanshu": 1,
        },
        "car": {
            "car": 1.5,
        },
    },
    "MP5K": {
        "poses": {
            "stand": 1,
            "squat": 0.67,
            "crawl": 0.53,
        },
        "muzzles": {
            "buchang-c": 0.6,
            "xiaoyan-c": 0.82,
        },
        "grips": {
            "zhijiao": 1,
            "banjie": 0.83,
            "qingxin": 0.75,
            "muzhi": 0.83,
        },
        "scopes": {
            "reddot": 0.52,
            "quanxi": 0.52,
            "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.45,
        },
        "stocks": {
            "zhongxing": 1,
            "zhanshu": 1,
        },
        "car": {
            "car": 1.5,
        },
    },
    "P90": {
        "poses"  : {
            "stand": 1,
            "squat" : 0.77,
            "crawl": 0.67,
        },
        "car"    : {
            "car" : 1.5,
        },
    },
    "JS9": {
        "poses": {
            "stand": 1,
            "squat": 0.73,
            "crawl": 0.5,
        },
        "muzzles": {
            "buchang-c": 0.58,
            "xiaoyan-c": 0.82,
        },
        "scopes": {
            "reddot": 0.52,
            "quanxi": 0.52,
            "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.45,
        },
        "car": {
            "car": 1.5,
        },
    },
    "MP9": {
        "poses": {
            "stand": 1,
            "squat": 0.73,
            "crawl": 0.63,
        },
        "scopes": {
            "reddot": 0.52,
            "quanxi": 0.52,
        },
        "stocks": {
            "zhedie": 1,
        },
        "car": {
            "car": 1.5,
        },
   },
    "M249": {
        "poses": {
            "stand": 1.28,
            "squat": 0.73,
            "crawl": 0.3,
        },
        "scopes": {
            "reddot": 0.55,
            "quanxi": 0.55,
	        "x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.45,
        },
        "stocks": {
			"zhanshu": 1,
			"zhongxing": 1,
        },
        "car": {
            "car": 1.5,
        },
    },
	"MG3": {
        "poses": {
            "stand": 3,
            "squat": 1.78,
            "crawl": 0.65,
        },
        "scopes": {
            "reddot": 0.52,
            "quanxi": 0.52,
			"x2": 1,
            "x3": 1.44,
            "x4": 2,
            "x6": 1.45,
        },
        "car": {
            "car": 1.5,
        },

    }
}

guns_trajectory = {
    "weapon_none": {
        "default": [16, 13, 11, 23, 14, 33, 17, 33, 18, 37, 19, 37, 19, 37, 21, 41, 21, 41, 21, 41, 21, 41, 21, 43, 22,
                    43, 22, 43, 22, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23]
    },
    "AKM": {
        "default": [16, 25, 13, 23, 16, 31, 16, 35, 20, 39, 21, 41, 21, 41, 21, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22,
                    43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22, 43, 22]
    },
    "M762": {
        "default": [18, 29, 17, 39, 21, 41, 21, 45, 25, 49, 25, 49, 25, 49, 29, 57, 30, 59, 30, 59, 30, 59, 30, 59, 30,
                    59, 30, 59, 30, 59, 30, 59, 30, 59, 30, 59, 30, 59, 30, 59, 30]
    },
    "G36C": {
        "default": [16, 13, 11, 23, 14, 33, 17, 33, 18, 37, 19, 37, 19, 37, 21, 41, 21, 41, 21, 41, 21, 41, 21, 43, 22,
                    43, 22, 43, 22, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23]
    },
    "M416": {
        "default": [16, 13, 11, 23, 14, 33, 17, 33, 18, 37, 19, 37, 19, 37, 21, 41, 21, 41, 21, 41, 21, 41, 21, 43, 22,
                    43, 22, 43, 22, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23]
    },
    "M16A4": {
        "default": [6, 11, 7, 13, 8, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23, 12, 23,
                    12, 23, 23, 21, 11, 21, 11, 21, 23, 23, 12, 23, 12, 23, 12, 23]
    },
    "SCARL": {
        "default": [16, 13, 11, 23, 14, 33, 17, 33, 18, 37, 19, 37, 19, 37, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21,
                    41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21, 41, 21]
    },
    "MK47": {
        "default": [6, 11, 9, 17, 10, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14, 27, 14,
                    27, 14, 27, 14, 27, 14, 27]
    },
    "QBZ": {
        "default": [16, 13, 11, 23, 14, 33, 17, 33, 18, 37, 19, 37, 19, 37, 21, 41, 21, 41, 21, 41, 21, 41, 21, 43, 22,
                    43, 22, 43, 22, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23, 45, 23]
    },
    "AUG": {
        "default":[18,17,9,25,16,35,20,39,20,41,23,49,25,49,26,51,27,53,27,53,27,53,27,53,27,53,27,53,27,53,27,55,28,55,28,55,28,55,28,55,28]
        },
    "GROZA": {
        "default": [16, 15, 13, 27, 14, 27, 14, 27, 14, 29, 15, 31, 16, 33, 18, 39, 20, 39, 20, 41, 21, 41, 21, 41, 21,
                    41, 21, 41, 21, 42, 21.5, 42, 21.5, 42, 21.5, 42, 21.5, 42, 21.5, 42, 21.5]
    },
    "ACE32": {
        "default":[18,23,12,29,17,37,20,39,21,41,21,43,23,45,23,45,23,47,25,51,26,51,26,51,27,53,27,53,27,53,27,53,27,53,27,53,27,53,27,53,27]
        },
    "K2": {
        "default": [16,13,11,23,14,33,17,33,18,37,19,37,19,37,21,41,21,41,21,41,21,41,21,41,21,41,21,41,21,41,21,41,21,41,21,41,21,41,21,41,21]
        },
    "FAMAS":{
        "default":[18,11,9,17,10,27,17,35,19,39,21,41,21,41,22,43,22,43,22,43,23,45,23,45,23,45,23,45,23,45,23,45,23,45,23,45,23,45,23,45,23]
      },
    "ZDZT": {
        "default": [5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9],
        "burst"  : [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    },
    "MINI14": {
        "default": [6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6,
                    11],
        "burst"  : [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    },
    "SKS": {
        "default": [4, 7, 4, 7, 4, 7, 4, 7, 4, 7, 4, 7, 4, 7, 4, 7, 4, 7, 4, 7],
        "DLG"    : [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    },
    "VSS": {
        "default": [5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9],
        "burst"  : [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    },
    "QBU": {
        "default": [6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11, 6, 11],
        "burst"  : [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    },
    "MK14": {
        "default": [5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9],
        "burst"  : [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    },
    "MK12": {
        "default": [5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9, 5, 9],
        "burst"  : [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    },
    "DLGNF": {
        "default": [9, 17, 9, 17, 9, 17, 9, 17, 9, 17, 9, 17, 9, 17, 9, 17, 9, 17, 9, 17],
        "burst"  : [20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
    },
    "PP19": {
        "default":[7,13,8,17,10,21,12,23,12,23,12,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5,20,10.5]
      },
    "TMX": {
        "default":[8,15,9,21,12,23,13,25,14,29,16,43,22,43,22,43,22,43,22,43,22,43,22,43,22,43,20,39,20,39,20,39,20,39,20,39,20,39,20,39,20,39,20,39,20,39,20,39,20,39]
      },
    "UMP": {
        "default":[9,17,10,21,12,25,13,25,14,27,14,28,14.5,28,14.5,28,14.5,28,14.5,28,14.5,28,14.5,28,14.5,28,14.5,28,14.5,28,14.5,28,14.5,28,14.5]
      },
    "UZI": {
        "default":[7,13,8,15,9,19,11,23,13,27,14,40,20.5,40,20.5,40,20.5,40,20.5,44,22.5,44,22.5,44,22.5,44,22.5,46,23.5,46,23.5,46,23.5,46,23.5]
      },
    "VECTOR":{
        "default":[11,19,11,23,13,27,15,31,17,33,19,40,22.5,48,27.5,54,27.5,54,27.5,54,27.5,54,27.5,54,27.5,54,27.5 ,54,27.5,54,27.5,54,27.5]
      },
    "MP5K": {
        "default":[16,17,9,23,14,29,16,33,18,37,19,37,19,38,19.5,38,19.5,38,19.5,38,19.5,38,19.5,38,19.5,38,19.5,38,19.5,38,20,39,20,39,20,39,20,39,20,39]
      },
    "P90":{
        "default":[8,15,9,21,12,23,13,25,13,23,14,27,15,29,12,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2,9.1,17.2]
      },
    "JS9":{
        "default":[10,13,7,19,12,25,13,25,13,25,13,25,15,36,18.5,36,18.5,36,18.5,36,18.5,36,18.5,36,18.5,36,18.5,36,18.5,36,18.5,36,18.5,36,18.5,36,18.5,36,18.5,36]
      },
    "MP9":{
        "default":[7,13,8,15,9,19,11,23,12,23,12,24,12.,24,12.,24,12.,22,8.5,16,7.5,14,7.5,14,7.5,14,7.5,14,7.5,14,7.5,14,7.5,14,7.5 ]
      },
    "M249": {
        "default":[15,9,4,15,9,19,10,23,12,19,10,19,8,13,8,15,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13,7 ,13 ]

        },
    "MG3": {
        "default":[11,1,1,5,3,5,3,5,3,5,2,3,2,3,1,3,2,3,2,3,2,3,2,3,2,1,1,1,1,1,1,1,1,1,3,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2,3,2]
        },
}