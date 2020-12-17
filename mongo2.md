- limit() 读取指定数量的文档
	
	- db.集合名.find().limit(数量)
	
- skip() 跳过指定数量的文档
	
	- db.集合名.find().skip(数量)
	
- limit()和skip()可以同时使用,skip().limit()效率较高

- ￥where 自定义查询
	- db.stu.find({
		$where:function(){
			return this.age>30;}
	} )
	
- 投影: 显示需要的内容 
	- db.stu.find({条件},{name:1})
		- 最后一个{}内将需要的字段为1，不需要不设置
		- -id默认显示，若需要不显示则需要置为0
	
- 排序 sort()
  - db.stu.find().sort({字段:1,字段:1})
    - 1为升序，-1为降序
    - 可以多个字段按顺序排序
  
- 统计个数 count()

- 去重 distinct(字段,{条件})
  - db.stu.find().distinct(字段)
  - 返回结果为去重后列表
  - 若需要过滤后的数据去重，可以在{}内添加条件
  
- 备份
  - mongodump -h dbhost -d dbname -o dbdirectory
    - -h 服务器地址，也可以指定端口号
    - -d 需要备份的数据库名称
    - -o 备份的数据存放的位置，目录
  
- 回复
  - mongorestore -h dbhost -d dbname --dir dbdirectory
    - -h 服务器地址
    - -d 需要恢复的数据库实例，恢复数据库名
    - --dir 备份数据所在位置
  
- 聚合 aggregate
  - db.集合名.aggregate({管道:{表达式}})
    - 可以有多个管道，前一个管道的输出结果当成下一个管道的输入，最后一个管道的输出即输出的数据
  
- 常用管道
  - $group ：将集合中的文档分组，可用于统计结果
  	```
      需要哪个属性需要加上$
      db.stu.aggregate(
        {$group:{_id:"gender", count:{$sum:1}, avg_age:{$avg:"$age"}}}
      )
      
      统计整个文档
      db.stu.aggregate(
        {$grouop:{_id:null, count:{$sum:1}, avg_age:{$avg:"$age"}}}
      )
	  ```
	  
	  ```
      测试
  		{"country":"china", "province":"sh", "userid":"a"} 
	      {"country":"china", "province":"sh", "userid":"b"}
    	{"country":"china", "province":"sh", "userid":"a"}
  	    {"country":"uk", "province":"sh", "userid":"c"}
  	    {"country":"china", "province":"bj", "userid":"da"}
  	    {"country":"china", "province":"bj", "userid":"fa"}
        db.test.insert({"country":"china", "province":"sh", "userid":"a"} )
  	    db.test.insert({"country":"china", "province":"sh", "userid":"b"} )
  	    db.test.insert({"country":"china", "province":"sh", "userid":"a"} )
  	    db.test.insert({"country":"uk", "province":"sh", "userid":"c"} )
  	    db.test.insert({"country":"china", "province":"bj", "userid":"da"} )
  	    db.test.insert({"country":"china", "province":"bj", "userid":"fa"} )
  	  统计每个country/province下的userid的数量(同一个userid只统计一次)
  	  	db.test.aggregate(
  	  		{$group:{_id:{country:"$country", province:"$province", userid:"$userid"}}},
  	  		{$group:{_id:{country:"$_id.country", province:"$_id.province"}, count:{$sum:1}}},
  	  		{$project:{country:"$_id.country", province:"$_id.province", count:1, _id:0}}
  	  	)
  	  	db.test.aggregate({$group:{_id:{country:"$country", province:"$province", userid:"$userid"}}},{$group:{_id:{country:"$_id.country", province:"$_id.province"}, count:{$sum:1}}},{$project:{country:"$_id.country", province:"$_id.province", count:1, _id:0}})
  	```
  	
  	```
      测试2
	    {"username":"Alex", "tags":["C#", "Java", "C++"]}
      获取tag列表的长度
      db.test2.aggregate(
      	{$match:{"username":"Alex"}},
      	{$unwind:{"$tags"}},
      	{$group:{_id:null,tags_count:{$sum:1}}},
      	{$project:{tags_count:1, _id:0}}
      )
      
      db.test2.aggregate({$match:{"username":"Alex"}},{$unwind:"$tags"},{$group:{_id:null,tags_count:{$sum:1}}},{$project:{tags_count:1, _id:0}})
    ```
    
  - $match ：过滤数据，只输出符合条件的文档
  
  - $peoject ：修改出入文档的结果，如重命名，增加，删除字段，创建计算结果
  
  - $sort ：将输入文档排序后输出
  
  - $limit ：限制聚合管道返回的文档数
  
  - $skip ：跳过指定数量的文档，并返回剩下的文档
  
  - $unwind ：将数组类型的字段进行拆分
  
    - 属性perserveNullAndEmptyArrays值为true表示保留属性值为空的文档
     ```
       db.test.aggregate({
       		$unwind:{
       			path:"$字段名",
     			perserveNullAndEmptyArrays:true
       		}
       })
       
     ```
  
- 常用表达式
  - $sum ：计算求和，$sum:1 表示以一倍计数
  - $avg ：计算平均值
  - $min ：获取最小值
  - $max ：获取最大值
  - $push ：在结果文档中插入值到一个数组中
  - $first ：根据资源文档的排序获取第一个文档数据
  - $last ：根据资源文档的排序获取最后一个文档数据
  
- 索引 ensureIndex

  - 建立唯一索引
    - db.集合.ensureIndex({属性1:1})，1代表升序，2代表降序
    - db.test4.ensureIndex({name:1})
    - 若添加{"unique":true}，则索引的值唯一
    - db.test4.ensureIndex({name:1},{"unique":true} )
  - 建立联合索引
    - db.集合.ensureIndex({属性1:1,属性2:1})
  - 查看所有索引
    - db.test.getIndexs()
    - 默认索引为_id
  - 删除索引
    - db.test.dropIndex({"索引名"})

- 查询时间 explain("executionStats")

  - db.test.find().explain("executionStats")