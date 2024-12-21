"""
CREATE TABLE `douban_movie` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '特定ID',
  `movie_name` varchar(100) NOT NULL COMMENT '电影名称',
  `movie_date` varchar(100) NOT NULL COMMENT '电影上映时间',
  `movie_score` varchar(100) NOT NULL COMMENT '电影评分',
  `movie_num` varchar(100) NOT NULL COMMENT '电影评论数',
  `movie_time` varchar(100) NOT NULL COMMENT '电影评时长',
  `movie_type` varchar(100) DEFAULT NULL COMMENT '电影评类型',
  `movie_director` varchar(100) DEFAULT NULL COMMENT '导演',
  `movie_actors` varchar(1000) DEFAULT NULL COMMENT '演员',
  `movie_url` varchar(1000) DEFAULT NULL COMMENT '影片链接',
  `movie_picture` varchar(1000) DEFAULT NULL COMMENT '海报链接',
  `movie_Introduction` varchar(1000) DEFAULT NULL COMMENT '影片简介',
  PRIMARY KEY  (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='top250'

"""