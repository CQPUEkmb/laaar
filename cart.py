
# 商品类
class goods:
    def __init__(self,name,sale,math,all):
        self.name = name        # 商品名称
        self.sale = sale        # 商品价格
        self.math = math        # 商品数量
        self.all = sale*math    # 总价（价格 × 数量）


# 购物车类
class car:
    def __init__(self):
        self.__car__ = []       # 购物车列表，用来存商品

    # 添加商品
    def add(self):
        name = input('商品名称：')          # 输入商品名称
        sale = int(input ('价格：'))        # 输入价格
        math = int(input('数量：'))         # 输入数量
        all = sale*math                     # 计算总价
        for i in self.__car__:              # 遍历购物车，检查该商品是否已存在
            if i.name == name:
                print('你不是买了吗')        # 已存在就提示，不再添加
                return

        goo = goods(name, sale, math,all)   # 创建商品对象
        # print(sale*math)
        self.__car__.append(goo)            # 加入购物车
        print('总价格为:',all)

    # 修改商品
    def change(self):
        name = input('你想改什么：')         # 输入要修改的商品名称
        for i in self.__car__:              # 找到该商品
            if i.name == name:
                print(f'该商品：{i.name}，价格：{i.sale}，数量：{i.math},总价{i.all}')   # 先显示原来的信息
                new_name = input('新名称：')             # 输入新名称
                new_sale = int(input('新价格：'))        # 输入新价格
                new_math = int(input('新数量：'))        # 输入新数量
                i.sale = new_sale                       # 更新价格
                i.math = new_math                       # 更新数量
                i.all = new_sale*new_math               # 重新算总价
                return
        print('没有你咋修改')                # 没找到

    # 删除商品
    def remove(self):
        name = input('你要删除什么商品?:')   # 输入要删除的商品名称

        for r in self.__car__:              # 找到该商品
            if r.name == name:
                self.__car__.remove(r)      # 从购物车中删除
                print('删除完成')
                return
        print('没有咋删除')                  # 没找到

    # 查看所有商品
    def show(self):
        total = 0                           # 所有商品的总价
        for n in self.__car__:              # 逐个显示商品
            print(f'商品：{n.name}，价格：{n.sale}，数量：{n.math},总价{n.all}')
            total += n.all                  # 累加总价
        print('全部价格为:',total)

    # 查看单个商品
    def check(self):
        name = input('哪一个商品')           # 输入要查询的商品名称
        for i in self.__car__:              # 找到该商品
            if i.name == name:
                print(f'商品信息：{i.name}，价格：{i.sale}，数量：{i.math}')   # 显示商品信息
                return
        print('没有')                        # 没找到


c = car()                        # 创建购物车对象
while True:                      # 循环显示菜单，直到退出
    print('\n===== 购物车 =====')
    print('1. 添加商品')
    print('2. 修改商品')
    print('3. 删除商品')
    print('4. 查看所有商品')
    print('5. 查看单个商品')
    print('0. 退出')
    choice = input('请选择功能：')    # 输入功能编号

    if choice == '1':
        c.add()                  # 添加商品
    elif choice == '2':
        c.change()               # 修改商品
    elif choice == '3':
        c.remove()               # 删除商品
    elif choice == '4':
        c.show()                 # 查看所有商品
    elif choice == '5':
        c.check()                # 查看单个商品
    elif choice == '0':
        print('退出成功')
        break                    # 退出程序
    else:
        print('输入错误，请重新选择')  