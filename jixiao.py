import os
import pandas as pd
import re
import os
import pandas as pd
import re
class jixiao(object):

    biyaozhibiao_name = ['数量', '质量', '时效', '成本', '社会效益']
    kece_name = ['数量', '质量', '时效', '成本']
    qitazhibiao_name = ['经济效益', '生态效益', '可持续影响', '服务对象满意度', '其他满意度']
    def __init__(self) -> None:
        self.xiangmu_path = None
        self.koujing_summary_dict = None
        self.zhengze = None
        self.bianma = None
        self.num = 0

    def shenhe_init(self):
        koujing = pd.read_excel('./审核口径模板.xlsx',header=1,index_col="编码")
        self.shenhe_dict = koujing[["审核细项","审核意见表述（问题+建议）"]]
        self.shenhe_muban = koujing[["审核要点","审核细项","审核意见表述（问题+建议）"]]
        self.wanzheng_dict = koujing.loc[koujing["审核要点"]=="完整性"]
        zhengze = koujing.loc[(koujing["模式"]=="正则匹配") & (koujing["正则表达式"] !="空"),"正则表达式"]
        self.zhengze = zhengze.to_dict()
        for key in self.zhengze:
            self.zhengze[key] = re.compile(self.zhengze[key],re.S)
        self.data = pd.read_excel("./项目信息.xlsx",sheet_name="data",na_values="")
        self.shenhe_info = pd.read_excel("./项目信息.xlsx",sheet_name="审核信息",na_values="")
        self.bianma_list = self.shenhe_info["项目编码"].to_list()

    def read_item(self,xiangmu_path):
        global xiangmu
        bianma_list = []
        xiangmu_info = []
        zhibiao_data = pd.DataFrame(columns=["项目编码","一级指标","二级指标","三级指标","指标值","指标解释"])
        for x in list(filter(lambda s:not s.startswith("."),os.listdir(xiangmu_path))):
            excel = pd.ExcelFile(xiangmu_path+"/"+x,engine="openpyxl")
            item_list = excel.sheet_names
            for y in item_list:
                y_i = excel.parse(y)
                bianma = str(int(y_i.iloc[0,1]))
                bianma_list.append(bianma)
                danwei = y_i.iloc[1,1]
                yiji_danwei = y_i.iloc[1,4]
                xiangmu_name = y_i.iloc[0,4]
                xiangmu_zongjine = y_i.iloc[4,1]
                bennian_jine = y_i.iloc[4,4]
                zhengceyiju = y_i.iloc[5,1]
                cesuanyiju = y_i.iloc[6,1]
                niandumubiao = y_i.iloc[7,1]
                xiangmu_info.append({"项目编码": bianma,"项目名称": xiangmu_name , "申请单位": danwei,"一级预算单位": yiji_danwei,"项目总金额": xiangmu_zongjine,"本年金额": bennian_jine,"政策依据": zhengceyiju,"测算依据": cesuanyiju,"年度目标": niandumubiao})
                jixiaozhibiao = y_i.iloc[10:-1,:]
                jixiaozhibiao.columns = ["一级指标","二级指标","三级指标","指标值","指标解释"]
                jixiaozhibiao.insert(0,"项目编码",bianma)
                zhibiao_data = pd.concat([zhibiao_data,jixiaozhibiao],ignore_index=True)
        xiangmu_info_data = pd.DataFrame(xiangmu_info).set_index("项目编码")
        zhibiao_data = zhibiao_data.set_index("项目编码")
        xiangmu = xiangmu_info_data.join(zhibiao_data)
        with pd.ExcelWriter('./项目信息.xlsx',engine="openpyxl") as writer:
            pd.DataFrame(data={"项目编码":bianma_list},columns=["项目编码","审核人","审核日期","完整性审核","可测性审核","可行性审核","初审小结"]).to_excel(writer,sheet_name="审核信息")
            xiangmu_info_data.to_excel(writer,sheet_name="项目信息")
            zhibiao_data.to_excel(writer,sheet_name="指标信息")
            xiangmu.to_excel(writer,sheet_name="data")

    def data_unit(self):
        data_unit = self.data.loc[self.data["项目编码"]==self.bianma]
        return data_unit

    def wanzheng_shenhe(self):
        # 政策依据 为空
        options = 0
        global wanzheng_sm_list
        global wanzheng_list
        wanzheng_sm_list = []
        wanzheng_list = []
        if not self.data_unit()["政策依据"].str.contains(self.zhengze[0]).all():
            self.easy_shenhe_ap(0,options)
        if not self.data_unit()["测算依据"].str.contains(self.zhengze[1]).all():
            self.easy_shenhe_ap(1,options)
        if self.data_unit()["年度目标"].isnull().all():
            self.easy_shenhe_ap(2,options)
        if self.data_unit()["年度目标"].str.contains(self.zhengze[3]).all():
            self.easy_shenhe_ap(3,options)
        if self.data_unit().loc[self.data_unit()["二级指标"].isin(self.biyaozhibiao_name),"三级指标":"指标解释"].isnull().all().all():
            self.easy_shenhe_ap(4,options)
        if self.data_unit().loc[self.data_unit()["二级指标"]=="数量","三级指标":"指标解释"].isnull().all(axis=1).any():
            self.easy_shenhe_ap(5,options)
        if self.data_unit().loc[self.data_unit()["二级指标"]=="质量","三级指标":"指标解释"].isnull().all(axis=1).any():
            self.easy_shenhe_ap(6,options)
        if self.data_unit().loc[self.data_unit()["二级指标"]=="时效","三级指标":"指标解释"].isnull().all(axis=1).any():
            self.easy_shenhe_ap(7,options)
        if self.data_unit().loc[self.data_unit()["二级指标"]=="成本","三级指标":"指标解释"].isnull().all(axis=1).any():
            self.easy_shenhe_ap(8,options)
        if self.data_unit().loc[self.data_unit()["二级指标"]=="社会","三级指标":"指标解释"].isnull().all(axis=1).any():
            self.easy_shenhe_ap(9,options)
        if self.data_unit().loc[self.data_unit()["二级指标"].isin(self.qitazhibiao_name),"三级指标":"指标解释"].isnull().any().any():
            self.easy_shenhe_ap(10,options)
        zhibiao_nan = (self.data_unit()["二级指标"].isin(self.biyaozhibiao_name)) & self.data_unit()["指标值"].isnull()
        self.advanced_shenhe_ap(zhibiao_nan,16,options)
        zhibiaojieshi_nan = (self.data_unit()["二级指标"].isin(self.biyaozhibiao_name)) & (self.data_unit()["指标解释"].isnull())
        self.advanced_shenhe_ap(zhibiaojieshi_nan,17,options)
        rongchang_list = self.data_unit()["三级指标"].str.contains(self.zhengze[21])
        self.advanced_shenhe_ap(rongchang_list,21,options)

    def kece_shenhe(self):
        global kece_sm_list
        global kece_list
        kece_sm_list = []
        kece_list = []
        bukecelist = (self.data_unit()["二级指标"].isin(self.biyaozhibiao_name)) & (~self.data_unit()["指标值"].str.contains(self.zhengze[23]))
        self.advanced_shenhe_ap(x=bukecelist,i=23,options = 1)
    def kexing_shenhe(self):
        global kexing_sm_list
        global kexing_list
        kexing_sm_list = []
        kexing_list = []
        if self.data_unit().loc[self.data_unit()["二级指标"]=="时效","指标值"].str.contains(self.zhengze[25]).any():
            self.easy_shenhe_ap(25,2)
    def shenhe(self):
        for xiangmu in self.shenhe_info["项目编码"]:
            try:
                self.bianma = xiangmu
                self.wanzheng_shenhe()
                self.kece_shenhe()
                self.kexing_shenhe()
                sm = wanzheng_sm_list  + kece_sm_list + kexing_sm_list
                self.shenhe_info.loc[self.shenhe_info["项目编码"]==self.bianma,"初审小结"] = ordered2text(sm)
                self.shenhe_info.loc[self.shenhe_info["项目编码"]==self.bianma,"完整性审核"] = ordered2text(wanzheng_list)
                self.shenhe_info.loc[self.shenhe_info["项目编码"]==self.bianma,"可测性审核"] = ordered2text(kece_list)
                self.shenhe_info.loc[self.shenhe_info["项目编码"]==self.bianma,"可行性审核"] = ordered2text(kexing_list)
            except:
                print(xiangmu)
        self.shenhe_info.to_excel("./初审结果.xlsx",sheet_name="机器审核")
    def easy_shenhe_ap(self,i,options):
        if options == 0:
            wanzheng_sm_list.append(self.shenhe_dict.iloc[i,0])
            wanzheng_list.append(self.shenhe_dict.iloc[i,1])
        if options == 1:
            kece_sm_list.append(self.shenhe_dict.iloc[i,0])
            kece_list.append(self.shenhe_dict.iloc[i,1])
        if options == 2:
            kexing_sm_list.append(self.shenhe_dict.iloc[i,0])
            kexing_list.append(self.shenhe_dict.iloc[i,1])
    def advanced_shenhe_ap(self,x,i,options):
        if x.any():
            zhibiao_nan_row = self.data_unit().loc[x,:]
            name_list = []
            for row,item in zhibiao_nan_row.iterrows():
                name_list.append(item["二级指标"] + "指标" +"”" + item["三级指标"] + "“")
            if options ==0:
                wanzheng_sm_list.append(self.shenhe_dict.iloc[i,0])
                wanzheng_list.append("、".join(name_list)+self.shenhe_dict.iloc[i,1])
            if options ==1:
                kece_sm_list.append(self.shenhe_dict.iloc[i,0])
                kece_list.append("、".join(name_list)+self.shenhe_dict.iloc[i,1])
            if options ==2:
                kexing_sm_list.append(self.shenhe_dict.iloc[i,0])
                kexing_list.append("、".join(name_list)+self.shenhe_dict.iloc[i,1])
def ordered2text(yijian_raw:list):
    n = len(yijian_raw)
    if n == 0:
        yijian = "   审核通过"
    else:
        nl = list(range(1,n+1))
        yijian_list = []
        for x in range(n):
            yijian_list.append(str(nl[x])+". "+yijian_raw[x])
        yijian = "\n".join(yijian_list)
    return yijian
def deordered2list(yijian:str):
    y = [x[3:] for x in yijian.split('\n')]
    return y
