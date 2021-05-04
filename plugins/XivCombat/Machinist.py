from .LogicData import LogicData

"""
2866：分裂弹
2868：独头弹
2872：热弹
2876：整备
2874：虹吸弹
2870：散射
2873：狙击弹
17209：超荷
7410：热冲击
2864：炮塔
2878：野火
2890：弹射
16497：自动弩
16498：钻头
7414：枪管加热
16499：毒菌
"""


def machinist_logic(data: LogicData):
    if data.target.effectiveDistanceX > 24: return
    hsid = 2872 if data.me.level < 76 else 16500
    single = data.is_single(dis=8, limit=3)
    if data.gcd > 1.1:
        if data.nAbility:
            return data.nAbility
        if min(data[2874], data[2890]) < 15:
            return 2874 if data[2874] <= data[2890] else 2890
        if not data.is_violent: return
        if data.gauge.battery >= 90:
            return 2864
        if not (data[16498] and data[hsid]) and not data[2876]: return 2876
        can_over = not data.gauge.overheatMilliseconds and data[16498] > 8 and data[hsid] > 8 and data.combo_remain > 8 and data.gauge.heat >= 50
        if can_over and not data[2878]: return 2878
        if can_over and data[2878] > 8: return 17209
        if data.gauge.heat < 50 and not data[7414]: return 7414
        if min(data[2874], data[2890]) < 60:
            return 2874 if data[2874] <= data[2890] else 2890
        if data.gauge.battery >= 50:
            return 2864
    elif data.gcd < 0.2:
        if data.nSkill:
            return data.nSkill
        if data[2876] or not data.is_violent:
            if data.gcd >= data[16498]: return 16498 if single else data.lv_skill(16499, (72, 16498))
            if data.gcd >= data[hsid]: return hsid
        if single or data.target.effectiveDistanceX > 12 or data.me.level < 18:
            if data.gauge.overheatMilliseconds and data.me.level >= 35:
                return 7410
            elif data.combo_id == 2866:
                return data.lv_skill(2868, (2, 2866))
            elif data.combo_id == 2868:
                return data.lv_skill(2873, (26, 2866))
            else:
                return 2866
        else:
            return 16497 if data.gauge.overheatMilliseconds and data.me.level >= 52 else 2870


fight_strategies = {
    31: machinist_logic
}
