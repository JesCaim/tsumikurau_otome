# ==========================================
# 剧情脚本: c1_s1_eden_daily.rpy
# ==========================================

label c1_s1:
    
    # === 场景 1：早晨的校园走廊 ===
    scene bg school_hallway with fade
    
    # 播放一段轻松的日常 BGM (假设你有)
    # play music "audio/bgm/daily_school.ogg" fadein 2.0

    narrator_adv "私立百合丘学园的早晨，一如既往地喧嚣。"
    narrator_adv "在通往教室的走廊上，那个身影准时出现了。"

    # --- 示例：使用你的 Python 类方法显示立绘 ---
    # 这会调用 endoEden.show("happy") -> renpy.show("eden happy")
    $ endoEden.show("happy")
    
    $ endoEden.say("老师好，同学们早安。")
    
    narrator_adv "远藤伊甸是一个「平凡」的孩子。至少在表面上如此。"

    # --- 示例：立绘表情差分切换 ---
    # 切换到普通表情 (normal)
    $ endoEden.show("normal")
    
    $ endoEden.say("今天的测验准备得怎么样了？如果有不懂的地方，午休可以来问我。")
    
    narrator_adv "她有着恰到好处的成绩，恰到好处的朋友，恰到好处的生活。"

    # --- 示例：立绘移动 (Move Transition) ---
    # 为了表现她从中间走到旁边，给其他人让路
    # 注意：涉及位置移动时，建议使用 Ren'Py 原生语句，比封装的类更灵活
    show eden normal at left with move
    
    narrator_adv "但在她侧身让开道路的瞬间，某种令人不安的完美感在那双眼睛里一闪而过。"

    # --- 示例：内心独白 (切换到黑屏 NVL) ---
    scene black with dissolve
    
    narrator_nvl """
    没有人见过远藤伊甸哭泣。

    没有人见过远藤伊甸愤怒。

    她的存在就像一面过于洁净的镜子，映照出周围所有人的瑕疵。
    """
    
    nvl clear

    # === 场景 2：教室角落的窃窃私语 ===
    scene bg classroom with fade
    
    # 此时伊甸不在场，我们显示其他三位少女
    # 这里的 role1, role2, role3 对应你定义的 maidenNoble 等
    
    # 一次性显示三人：左、中、右
    show role1 normal at left
    show role3 normal at center
    show role2 normal at right
    with dissolve

    # 角色对话
    $ maidenNoble.say("喂，你们看到了吗？刚才我不小心把水洒在她鞋子上了。")
    
    $ maidenMerciful.say("她生气了吗？那双鞋子可是限定款...")
    
    # --- 示例：高贵少女切换表情 (假设有 angry 差分) ---
    # show role1 angry 
    $ maidenNoble.say("没有！她居然微笑着说'没关系'！")
    $ maidenNoble.say("她为什么不生气？正常人这时候都会发火吧？")

    $ maidenCalm.say("所以我才说...她不像人类。")
    $ maidenCalm.say("就像是一个被设定好程序的玩偶，永远维持着完美的运行参数。")

    # --- 示例：伊甸突然出现 (惊悚效果) ---
    # 隐藏其他人
    hide role1
    hide role2
    hide role3
    with dissolve
    
    # 伊甸突然出现在特写位置 (Zoom 放大)
    # 这里我们临时放大一下立绘，制造压迫感
    show eden happy at center:
        zoom 0.8 yalign 1.0 # 比默认的0.5大，形成特写
    with vpunch # 屏幕震动效果
    
    $ endoEden.say("大家在聊什么这么开心呢？")
    
    narrator_adv "她的声音总是那么平稳，平稳得让人怀疑其中是否真的蕴含情感。"
    
    # 切换为愤怒/阴暗表情 (对应你给的 angry 图片)
    show eden angry with dissolve
    
    $ endoEden.say("如果不快点回座位的话，上课就要迟到了哦。")
    
    narrator_adv "怀疑的种子一旦种下，就会在黑暗中悄然生长。"

    scene bg jiting with fade

    show eden happy
    $ endoEden.say("我要打舞萌！！！")

    show eden angry with vpunch
    $ endoEden.say("我要打舞萌！！！")

    show eden happy with vpunch
    $ endoEden.say("我操！！！！！！！！！")

    show eden angry with vpunch
    $ endoEden.say("一个人都没有！！！！！！！！！")

    show eden normal
    $ endoEden.say("...唔。")
    # 结束本节，跳转回流程控制
    jump start