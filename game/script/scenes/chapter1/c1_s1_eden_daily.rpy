label c1_s1:
    narrator_adv "远藤伊甸是一个「平凡」的孩子。"
    narrator_adv "至少在表面上如此。"
    narrator_adv "她有着恰到好处的成绩，恰到好处的朋友，恰到好处的生活。"
    narrator_adv "但在这恰到好处的表象之下，是某种令人不安的完美。"
    
    scene black with fade
    narrator_nvl """
    没有人见过远藤伊甸哭泣。

    没有人见过远藤伊甸愤怒。

    没有人见过远藤伊甸犯过错。

    她的存在就像一面过于洁净的镜子，映照出周围所有人的瑕疵。
    """
    
    nvl clear

    # 显示远藤伊甸 - 使用 endoEden
    show role7 at center with dissolve
    $ endoEden.say("早上好，今天天气真好呢。")
    narrator_adv "她的声音总是那么平稳，平稳得让人怀疑其中是否真的蕴含情感。"
    
    hide role7
    
    # 显示三位少女并让她们说话
    show role1 at left
    $ maidenNoble.say("她为什么不生气？我明明说了那么过分的话...")
    
    show role2 at right
    $ maidenMerciful.say("她为什么不哭泣？明明失去了那么重要的东西...")
    
    show role3 at center
    $ maidenCalm.say("她为什么不犯错？就像...就像不是人类一样。")
    
    narrator_adv "怀疑的种子一旦种下，就会在黑暗中悄然生长。"
    narrator_adv "而远藤伊甸，依然维持着她那完美的、令人毛骨悚然的平凡。"
    
    # 返回序幕，形成循环
    jump start