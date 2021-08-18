# Underwear plugins

所有的命令都是在聊天栏的默语频道（/e）输入，并且区分大小写

以下所有插件都会导致**封禁**，不提供任何技术支持，并随时可能失效

## CraftAutomation

自动制作

@ca

## CutsceneSkipper

动画城跳动画

@cutscene

## PosLocker

位置锁定（防击退）

@posL

## SkillAniUnlocker2

解除动画锁（十插）

@sALock

## Slider

滑步

@slide

## SpeedHack

加速

@speedH [get/set] [args]

## SuperJump

超级跳

@sjump [function] [args]

function

```
    [get]:      get current jump value
    [set]:      set current jump value
                format: /e @sjump set [value(float) / "default"]
```

## Teleporter

瞬移

@tp [function] [args]

function

```
    [get]:          get current coordinates
  
    [set]:          set current coordinates
                    format: /e @tp set [x:float] [y:float] [z:float]
  
    [list]:         list saved coordinates in current zone
  
    [save]:         save coordinates with a name
  
                    format: /e @tp save [name:str]
    [drop]:         drop a saved coordinates
  
                    format: /e @tp drop [name:str]
  
    [goto]:         goto a saved coordinates with 15 meters limit
                    format: /e @tp goto [name:str]
  
    [force-goto]:   goto a saved coordinates with no distance limit
                    format: /e @tp force-goto [name:str]

    relative coordinates teleport:
        format: /e @tp [direction] [distance:float]
        direction:  u/up,
                    d/down,
                    f/front,
                    l/left,
                    r/right,
                    b/back,
                    n/north,
                    e/east,
                    w/west,
                    s/south
```

## Facing

背对，必须保持移动才能保证背对

need Teleporter

@Facing

## ~~XivCombat~~

~~@aCombat [on/off] [s/m]~~

## CutTheTree

金蝶砍树，概率炸游戏，不负责售后

@CTT

```
    [on] 启动自动砍
    [off] 关闭自动砍
    [hack] 自动发包，可以先on再hack，估计会掉线，建议别用了
```

## SlaveDrive

虚空雇员，使用后无法与任何物件交互，除非小退游戏

@slave

```
[collect] 重复一次雇员探险
[auto] 自动进行雇员探险
```

## AFix

身位矫正（娱乐用）

@afix

## Rapper

缩短咏唱时间（不能减少gcd）

@rap [get/set] [float]

## EveryoneFat

扩大目标圈，1是极限

@fat [get/set] [float]
