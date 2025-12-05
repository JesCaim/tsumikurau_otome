# ==========================================
#                  资源定义
# ==========================================

# 1. 定义背景 
image bg school_hallway = "images/bg/school_hallway.png"
image bg classroom = "images/bg/classroom.png"

# 2. 定义伊甸的立绘 (应用缩放变换)
# 注意：这里对应 endoEden 初始化时的 image="eden"
image eden happy  = Transform("images/characters/eden/eden_happy.png", zoom=0.8, yalign=1.0)
image eden normal = Transform("images/characters/eden/eden_normal.png", zoom=0.8, yalign=1.0)
image eden angry  = Transform("images/characters/eden/eden_angry.png", zoom=0.8, yalign=1.0)

# 3. 定义其他角色的立绘 (对应 role1, role2...)
# image role1 normal = Transform("images/characters/noble_normal.png", zoom=0.5, yalign=1.0)
# image role2 normal = Transform("images/characters/merciful_normal.png", zoom=0.5, yalign=1.0)
# image role3 normal = Transform("images/characters/calm_normal.png", zoom=0.5, yalign=1.0)