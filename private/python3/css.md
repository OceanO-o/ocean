
CSS在HTML中的引用方式
    1. 外部样式表  css和html文件分开放，在html的head中引用 <link href="index.css" rel="stylesheet" type="text/css" />
    2. 内部样式表 放在head中用style
    3. 内联样式表 卸载标签里面
    
CSS选择器入门
    元素选择器   放在head style 里面 div{color:red;}
    id选择器  #lvye{color:red;}  用#号
    class选择器  .lv{color:red;} 用.
    子元素选择器  #father1 div{color:blue;} 或者 #father2 #p1{color:red;}
    相邻选择器   #lv+div{color:red;}  表示选择“id为lv的元素”的相邻的下一个兄弟元素div
    群组选择器   h3,div,p,span{color:red;}  两个选择器之间必须用“,”（英文逗号）隔开

字体样式
    color 字体颜色,颜色值是一个关键字或一个16进制的RGB值 #p1{color: #03FCA1;}
    font-family 字体类型 #p1{font-family:微软雅黑,Arial,Times New Roman;} 优先选择第一个没有则依次类推
    font-size 字体大小 #p2{ font-size: 15px;}
    font-weight 字体粗细，font-weight:粗细值; #p1{font-weight:lighter;}  normal lighter bold	 bolder 这几种值
    font-style  字体斜体样式，font-style:取值; #p1{font-style:normal;}  italic oblique
    CSS注释  /*注释的内容*/
    
文本样式
    text-decoration 下划线、删除线和顶划线  none underline line-through(删除线) overline(顶划线)
        去除标签中的下划线“<a href="http://www.lvyestudy.com">  a{text-decoration:none;}
    text-transform 文本大小写 #p3{text-transform:capitalize;} 首字母大写
    text-indent  首行缩进  text-indent:28px; text-indent的属性值应该是字体font-size属性值的两倍
    text-align  文本水平对齐，使用text-align属性控制文本的水平方向的对齐方式：左对齐、居中对齐、右对齐。
        left center right text-align属性只能针对文本文字和img标签
        #p3{text-align:right;}
    line-height  行高 #p3{line-height:20px;}
    letter-spacing字母间距和word-spacing词间距，这两个属性取值单位都是像素 #p3{word-spacing:5px;}

边框样式
    边框属性 border-width边框的宽度  border-style边框的外观 border-color边框的颜色
    设置一个元素的边框必须要同时设置border-width、border-style、border-color这三个属性，
    这个元素的边框才能在浏览器显示出来
    border-width:像素值;
    border-style属性用于设置边框的外观，例如实线边框和虚线边框。有 none hidden solid实线 dashed虚线 dotted点线 double双线，双线的宽度等于border-width值
    inset、outset、ridge和groove是用于定义3D边框样式，如果我们将border-width定义得比较小时，这几个属性值的效果几乎都一样，但是当border-width定义得足够大时，这几个属性值的区别就明显出来了。
    border-color:颜色值
            border-width:1px;
            border-style:solid;    ----> 相当于 border:1px solid Red; (简写)
            border-color:Red;
    边框border局部样式：
    上边框border-top  下边框border-bottom 左边框border-left 右边框border-right 可以分别设置：
            border-right-width:1px;
            border-right-style:solid;   ---> border-right:1px solid green;
            border-right-color:red;
            
背景样式
    背景样式主要包括背景颜色和背景图像
    background-color 背景颜色  #div2{background-color: #F3DE3F;}
    背景图像:
        background-image	定义背景图像的路径，这样图片才能显示
            background-image:url("../App_images/lesson/run_cj/one piece.jpg");
            给某个元素设置背景图像，元素要有一定的宽度和高度，背景图片才会显示出来
        background-repeat属性定义背景图像的显示方式，例如不平铺、横向平铺和两个方向都平铺。
            background-repeat:取值; no-repeat表示不平铺 repeat表示在水平方向（x轴）和垂直方向（y轴）同时平铺 repeat-x表示在水平方向（x轴）平铺  repeat-y
        background-position属性定义了背景图像在该元素的位置
            background-position:像素值/关键字;
            背景位置属性用于设置背景图像的位置，这个属性只能应用于块级元素和替换元素。其中替换元素包括img、input、textarea、select和object。
            background-position:像素值/关键字; “background-position：12px 24px;” 12设置网页的横向位置，单位为px
            top left左上 top center靠上居中 top right右上  background-position:right center;
        background-attachment属性可以设置背景图像是随对象滚动还是固定不动。
            background-attachment:scroll/fixed;
            scroll表示背景图像随对象滚动而滚动，是默认选项；
            在IE或者360中设置background-attachment之后不能设置background-position属性，不然图片没办法在浏览器显示。可以测试一下google浏览器、Firefox浏览器。

超链接样式
    text-decoration:none”来去除超链接下划线
    定义超链接伪类
        a:link{CSS样式}	定义a元素未访问时的样式
        a:visited{CSS样式}	定义a元素访问后的样式
        a:hover{CSS样式}	定义鼠标经过显示的样式
        a:active{CSS样式}	定义鼠标单击激活时的样式    a:link{CSS样式}
        love hate爱恨原则， l v h a
                        a{text-decoration:none;font-size:18px;}
                        a:link{color:white}
                        a:visited{color: purple; }
                        a:hover{color:yellow;text-decoration:underline;}
                        a:active{color:red;}
    hover伪类
        “:hover”只限于a标签，“:hover”伪类可以定义任何一个元素在鼠标经过时的样式！
         元素:hover{}, “元素”可以是任意的块元素和行内元素。
    cursor属性来定义鼠标的样式
        cursor:pointer; 在div里面是手， cursor:default; 在div里面就是正常箭头
        
图片样式
    width和height,图片的大小，我们也是用width和height来定义
    对于图片的边框，我们也是使用border属性来定义 border:1px solid gray;
    text-align只对文本和img标签有效，对其他标签无效。text-align:属性值; left默认值，左对齐 center居中对齐 right右对齐
        图片是要在父元素中进行水平对齐的,在例子中，img元素的父元素是div，img元素是相对于div元素进行水平对齐的
    vertical-align 图片垂直对齐
    float 文字环绕效果
        float:取值; left元素向左浮动 right元素向右浮动
    
列表样式
表格样式
CSS盒子模型
    {
        display:inline-block; /*将块元素转换为inline-block元素*/
        padding:20px;
        margin:40px;
        border:1px solid red;
        background-color:#FCE9B8;
    }      

浮动布局
    浮动 float:取值;
    清楚浮动 clear:取值;  left right both
    
定位布局
    fixed 固定定位
        当元素的position属性设置为fixed时，这个元素就被固定了，被固定的元素不会随着滚动条的拖动而改变位置。在视野中，固定定位的元素的位置是不会改变的。
    relative 相对定位
        “position:relative;”
    absolute; 绝对定位
        “position:absolute;”是结合top、bottom、left和right这4个属性一起使用的
    static是position属性的默认值
    CSS固定定位元素和CSS绝对定位元素的位置是相对于浏览器而言，而CSS相对定位元素的位置是相对原始位置而言。
        