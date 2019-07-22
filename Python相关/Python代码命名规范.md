## 命名方法
---
#### 骆驼命名法（CamelCasing）
混合使用大小写字母来命名，但第一个单词的首字母为小写  
例如：`myVariable,myLabel`

#### 帕斯卡命名法（PascalCasing）
混合使用大小写字母来命名，第一个单词的首字母就要为大写  
例如：`MyVariable,MyLabel`

#### 匈牙利命名法（HungarianCasing）
变量名=属性+类型+对象描述  
例如：`hwnd` 窗口句柄, `pfnEatApple`  表示指向 `EatApple` 函数的函数指针变量

#### 下划线命名法（UnderScoreCasing）
每个单词之间用下划线连接  
例如：``your_are_handsome

## python代码命名规则
---
| Type | Public | Intermal |  
| - | :-: | -: |     
Modules | lower_with_under | _lower_with_under  
Classes	| CapWords | _CapWords
Exceptions | CapWords	 
Functions | lower_with_under() | _lower_with_under()
Global/Class Constants|	CAPS_WITH_UNDER | _CAPS_WITH_UNDER
Global/Class Variables	|lower_with_under | _lower_with_under
Instance Variables | lower_with_under | _lower_with_under (protected) or __lower_with_under (private)
Method Names | lower_with_under() | _lower_with_under() |(protected) or __lower_with_under() (private)
Function/Method Parameters | lower_with_under	 
Local Variables	| lower_with_under	 