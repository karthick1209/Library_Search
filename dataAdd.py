import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','demoProject.settings')

import django
django.setup()
from libApp.models import *

book_data = [{
  "book_title": "mauris enim leo rhoncus sed vestibulum sit amet cursus id turpis integer aliquet massa id lobortis convallis tortor risus",
  "author": "Mady Michin",
  "publication_date": "2020-08-19",
  "genre": "romance",
  "publisher": "Realbuzz",
  "num_pages": 234,
  "language": "Arabic",
  "rating": 4.5,
  "available": True
}, {
  "book_title": "id sapien in sapien iaculis congue vivamus metus arcu adipiscing molestie hendrerit at vulputate vitae",
  "author": "Benji Blewis",
  "publication_date": "2006-12-07",
  "genre": "mystery",
  "publisher": "Dablist",
  "num_pages": 725,
  "language": "Bosnian",
  "rating": 4.3,
  "available": True
}, {
  "book_title": "enim blandit mi in porttitor pede justo eu massa donec dapibus",
  "author": "Jim Dumbare",
  "publication_date": "2021-01-04",
  "genre": "mystery",
  "publisher": "Agimba",
  "num_pages": 237,
  "language": "Chinese",
  "rating": 3.8,
  "available": False
}, {
  "book_title": "facilisi cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel",
  "author": "Astrid Pyzer",
  "publication_date": "2018-03-17",
  "genre": "non-fiction",
  "publisher": "Lajo",
  "num_pages": 521,
  "language": "Macedonian",
  "rating": 3.5,
  "available": True
}, {
  "book_title": "leo odio condimentum id luctus nec molestie sed justo pellentesque viverra",
  "author": "Toddy Deverale",
  "publication_date": "2000-10-26",
  "genre": "mystery",
  "publisher": "Dynabox",
  "num_pages": 476,
  "language": "Czech",
  "rating": 3.7,
  "available": True
}, {
  "book_title": "dictumst morbi vestibulum velit id pretium iaculis diam erat fermentum justo nec condimentum neque sapien placerat ante nulla justo",
  "author": "Shandra Thow",
  "publication_date": "2014-09-08",
  "genre": "non-fiction",
  "publisher": "Edgeclub",
  "num_pages": 255,
  "language": "Swati",
  "rating": 2.6,
  "available": False
}, {
  "book_title": "vitae nisi nam ultrices libero non mattis pulvinar nulla pede ullamcorper augue a suscipit nulla elit",
  "author": "Nana Witheridge",
  "publication_date": "2002-03-10",
  "genre": "fiction",
  "publisher": "Brightdog",
  "num_pages": 474,
  "language": "Dari",
  "rating": 4.5,
  "available": False
}, {
  "book_title": "sapien cum sociis natoque penatibus et magnis dis parturient montes",
  "author": "Gnni Minter",
  "publication_date": "2001-12-10",
  "genre": "romance",
  "publisher": "Yacero",
  "num_pages": 610,
  "language": "Kurdish",
  "rating": 3.9,
  "available": True
}, {
  "book_title": "tristique fusce congue diam id ornare imperdiet sapien urna pretium nisl ut volutpat sapien arcu sed augue aliquam",
  "author": "Brandi Kimm",
  "publication_date": "2014-03-04",
  "genre": "non-fiction",
  "publisher": "Tagopia",
  "num_pages": 49,
  "language": "Finnish",
  "rating": 4.8,
  "available": True
}, {
  "book_title": "in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit",
  "author": "Farris Muzzall",
  "publication_date": "2011-12-20",
  "genre": "fiction",
  "publisher": "Demimbu",
  "num_pages": 683,
  "language": "Tetum",
  "rating": 2.2,
  "available": True
}, {
  "book_title": "id consequat in consequat ut nulla sed accumsan felis ut at dolor quis odio consequat",
  "author": "Clarke Yerson",
  "publication_date": "2015-08-27",
  "genre": "non-fiction",
  "publisher": "Skyba",
  "num_pages": 451,
  "language": "French",
  "rating": 2.8,
  "available": False
}, {
  "book_title": "vestibulum aliquet ultrices erat tortor sollicitudin mi sit amet lobortis sapien sapien non mi",
  "author": "Klarika Bere",
  "publication_date": "2019-08-01",
  "genre": "romance",
  "publisher": "Skimia",
  "num_pages": 958,
  "language": "Irish Gaelic",
  "rating": 3.3,
  "available": True
}, {
  "book_title": "rutrum at lorem integer tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat praesent",
  "author": "Daveta McGruar",
  "publication_date": "2013-01-23",
  "genre": "non-fiction",
  "publisher": "Oyondu",
  "num_pages": 641,
  "language": "Tetum",
  "rating": 4.1,
  "available": True
}, {
  "book_title": "magnis dis parturient montes nascetur ridiculus mus vivamus vestibulum sagittis sapien cum",
  "author": "Octavius Swiffen",
  "publication_date": "2014-06-03",
  "genre": "fiction",
  "publisher": "Yadel",
  "num_pages": 389,
  "language": "Icelandic",
  "rating": 3.7,
  "available": True
}, {
  "book_title": "arcu sed augue aliquam erat volutpat in congue etiam justo etiam pretium iaculis justo in hac",
  "author": "Freddy Bugby",
  "publication_date": "2021-09-26",
  "genre": "non-fiction",
  "publisher": "Skaboo",
  "num_pages": 164,
  "language": "Chinese",
  "rating": 3.6,
  "available": False
}, {
  "book_title": "lacinia nisi venenatis tristique fusce congue diam id ornare imperdiet sapien urna pretium nisl ut volutpat sapien arcu",
  "author": "Marylinda Mingey",
  "publication_date": "2016-05-06",
  "genre": "romance",
  "publisher": "Meejo",
  "num_pages": 467,
  "language": "Danish",
  "rating": 1.8,
  "available": False
}, {
  "book_title": "at vulputate vitae nisl aenean lectus pellentesque eget nunc donec quis",
  "author": "Michal Strass",
  "publication_date": "2002-05-21",
  "genre": "fiction",
  "publisher": "Topicshots",
  "num_pages": 935,
  "language": "Zulu",
  "rating": 4.5,
  "available": False
}, {
  "book_title": "sagittis sapien cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus etiam vel augue vestibulum rutrum",
  "author": "Helen-elizabeth Holehouse",
  "publication_date": "2003-07-16",
  "genre": "mystery",
  "publisher": "Roomm",
  "num_pages": 274,
  "language": "Latvian",
  "rating": 4.2,
  "available": False
}, {
  "book_title": "vitae nisl aenean lectus pellentesque eget nunc donec quis orci eget orci vehicula condimentum curabitur in",
  "author": "Aubry Cecil",
  "publication_date": "2007-01-06",
  "genre": "fiction",
  "publisher": "Yamia",
  "num_pages": 88,
  "language": "Azeri",
  "rating": 4.3,
  "available": True
}, {
  "book_title": "ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae donec pharetra magna vestibulum",
  "author": "Boyce Challoner",
  "publication_date": "2013-02-27",
  "genre": "fiction",
  "publisher": "Wikizz",
  "num_pages": 597,
  "language": "English",
  "rating": 1.3,
  "available": True
}, {
  "book_title": "eu felis fusce posuere felis sed lacus morbi sem mauris",
  "author": "Arlee Robillard",
  "publication_date": "2008-02-23",
  "genre": "non-fiction",
  "publisher": "Cogibox",
  "num_pages": 545,
  "language": "Swahili",
  "rating": 4.7,
  "available": False
}, {
  "book_title": "luctus et ultrices posuere cubilia curae donec pharetra magna vestibulum aliquet ultrices erat tortor",
  "author": "Dilly Holworth",
  "publication_date": "2002-03-24",
  "genre": "fiction",
  "publisher": "Trudeo",
  "num_pages": 512,
  "language": "Icelandic",
  "rating": 1.4,
  "available": True
}, {
  "book_title": "duis aliquam convallis nunc proin at turpis a pede posuere nonummy integer",
  "author": "Rivalee Zuanazzi",
  "publication_date": "2016-08-26",
  "genre": "romance",
  "publisher": "Oyoyo",
  "num_pages": 968,
  "language": "Punjabi",
  "rating": 4.8,
  "available": False
}, {
  "book_title": "nulla suscipit ligula in lacus curabitur at ipsum ac tellus semper interdum mauris ullamcorper purus sit amet nulla",
  "author": "Conway Alps",
  "publication_date": "2008-12-24",
  "genre": "mystery",
  "publisher": "Vitz",
  "num_pages": 884,
  "language": "Kurdish",
  "rating": 4.7,
  "available": True
}, {
  "book_title": "ut massa quis augue luctus tincidunt nulla mollis molestie lorem quisque",
  "author": "Sonni Rubinfeld",
  "publication_date": "2010-12-25",
  "genre": "fiction",
  "publisher": "Tanoodle",
  "num_pages": 294,
  "language": "Malagasy",
  "rating": 1.5,
  "available": False
}, {
  "book_title": "nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel nulla eget eros elementum pellentesque quisque",
  "author": "Clementina Whaley",
  "publication_date": "2010-09-29",
  "genre": "non-fiction",
  "publisher": "Mydeo",
  "num_pages": 792,
  "language": "Hiri Motu",
  "rating": 1.5,
  "available": False
}, {
  "book_title": "magnis dis parturient montes nascetur ridiculus mus etiam vel augue vestibulum rutrum rutrum neque aenean auctor gravida sem praesent id",
  "author": "Marne Tuvey",
  "publication_date": "2008-02-26",
  "genre": "mystery",
  "publisher": "Kwideo",
  "num_pages": 455,
  "language": "Albanian",
  "rating": 2.2,
  "available": True
}, {
  "book_title": "ac tellus semper interdum mauris ullamcorper purus sit amet nulla quisque arcu libero rutrum ac lobortis vel dapibus at diam",
  "author": "Lavena Broadbent",
  "publication_date": "2022-10-26",
  "genre": "non-fiction",
  "publisher": "Skinder",
  "num_pages": 712,
  "language": "Romanian",
  "rating": 1.6,
  "available": False
}, {
  "book_title": "et ultrices posuere cubilia curae mauris viverra diam vitae quam suspendisse",
  "author": "Rochella Simnel",
  "publication_date": "2007-10-19",
  "genre": "romance",
  "publisher": "Tagchat",
  "num_pages": 432,
  "language": "Japanese",
  "rating": 4.2,
  "available": False
}, {
  "book_title": "donec odio justo sollicitudin ut suscipit a feugiat et eros vestibulum ac est lacinia nisi",
  "author": "Mersey Gogerty",
  "publication_date": "2008-09-16",
  "genre": "mystery",
  "publisher": "Riffpath",
  "num_pages": 520,
  "language": "Quechua",
  "rating": 1.1,
  "available": True
}, {
  "book_title": "vestibulum velit id pretium iaculis diam erat fermentum justo nec condimentum neque sapien placerat",
  "author": "Lawrence Arington",
  "publication_date": "2013-04-29",
  "genre": "romance",
  "publisher": "Yakitri",
  "num_pages": 424,
  "language": "Spanish",
  "rating": 4.7,
  "available": True
}, {
  "book_title": "pulvinar sed nisl nunc rhoncus dui vel sem sed sagittis nam congue",
  "author": "Alaric Tedahl",
  "publication_date": "2016-10-27",
  "genre": "mystery",
  "publisher": "Thoughtstorm",
  "num_pages": 545,
  "language": "Greek",
  "rating": 4.0,
  "available": True
}, {
  "book_title": "justo sollicitudin ut suscipit a feugiat et eros vestibulum ac est lacinia nisi venenatis tristique fusce congue diam id",
  "author": "Adair Simmonds",
  "publication_date": "2013-10-30",
  "genre": "romance",
  "publisher": "Trupe",
  "num_pages": 412,
  "language": "Catalan",
  "rating": 2.1,
  "available": True
}, {
  "book_title": "quam sapien varius ut blandit non interdum in ante vestibulum ante ipsum primis",
  "author": "Nessie Dutnall",
  "publication_date": "2003-09-20",
  "genre": "fiction",
  "publisher": "Miboo",
  "num_pages": 138,
  "language": "Filipino",
  "rating": 2.4,
  "available": False
}, {
  "book_title": "etiam vel augue vestibulum rutrum rutrum neque aenean auctor gravida sem praesent id",
  "author": "Agneta Ipwell",
  "publication_date": "2014-06-17",
  "genre": "fiction",
  "publisher": "Brainverse",
  "num_pages": 170,
  "language": "Malay",
  "rating": 3.8,
  "available": True
}, {
  "book_title": "sit amet lobortis sapien sapien non mi integer ac neque duis bibendum morbi non quam nec dui luctus rutrum",
  "author": "Julie Klezmski",
  "publication_date": "2003-07-20",
  "genre": "non-fiction",
  "publisher": "Brainverse",
  "num_pages": 627,
  "language": "Filipino",
  "rating": 1.2,
  "available": True
}, {
  "book_title": "justo lacinia eget tincidunt eget tempus vel pede morbi porttitor lorem id",
  "author": "Dolph Duffitt",
  "publication_date": "2000-06-15",
  "genre": "non-fiction",
  "publisher": "Snaptags",
  "num_pages": 545,
  "language": "Yiddish",
  "rating": 2.2,
  "available": True
}, {
  "book_title": "quis orci eget orci vehicula condimentum curabitur in libero ut massa volutpat",
  "author": "Ludvig Raison",
  "publication_date": "2008-12-11",
  "genre": "mystery",
  "publisher": "Tazzy",
  "num_pages": 275,
  "language": "Bosnian",
  "rating": 2.4,
  "available": True
}, {
  "book_title": "volutpat dui maecenas tristique est et tempus semper est quam pharetra",
  "author": "Gayler Antoniak",
  "publication_date": "2004-11-15",
  "genre": "fiction",
  "publisher": "Meezzy",
  "num_pages": 935,
  "language": "Spanish",
  "rating": 2.3,
  "available": False
}, {
  "book_title": "vulputate vitae nisl aenean lectus pellentesque eget nunc donec quis orci eget orci vehicula",
  "author": "Price Diem",
  "publication_date": "2015-09-23",
  "genre": "non-fiction",
  "publisher": "Buzzshare",
  "num_pages": 824,
  "language": "Luxembourgish",
  "rating": 1.4,
  "available": True
}, {
  "book_title": "vulputate elementum nullam varius nulla facilisi cras non velit nec nisi vulputate nonummy",
  "author": "Mariam Wadwell",
  "publication_date": "2016-09-13",
  "genre": "non-fiction",
  "publisher": "Rooxo",
  "num_pages": 656,
  "language": "Swahili",
  "rating": 2.4,
  "available": True
}, {
  "book_title": "erat nulla tempus vivamus in felis eu sapien cursus vestibulum proin eu mi nulla ac",
  "author": "Chucho Phette",
  "publication_date": "2019-11-07",
  "genre": "mystery",
  "publisher": "Tambee",
  "num_pages": 14,
  "language": "Tsonga",
  "rating": 2.7,
  "available": False
}, {
  "book_title": "libero ut massa volutpat convallis morbi odio odio elementum eu",
  "author": "Marv Chesson",
  "publication_date": "2001-03-19",
  "genre": "fiction",
  "publisher": "Photolist",
  "num_pages": 952,
  "language": "Zulu",
  "rating": 2.9,
  "available": True
}, {
  "book_title": "luctus et ultrices posuere cubilia curae donec pharetra magna vestibulum aliquet ultrices erat",
  "author": "Merlina Shilstone",
  "publication_date": "2005-03-15",
  "genre": "mystery",
  "publisher": "Bubblebox",
  "num_pages": 134,
  "language": "Swedish",
  "rating": 2.6,
  "available": True
}, {
  "book_title": "lacus curabitur at ipsum ac tellus semper interdum mauris ullamcorper purus",
  "author": "Rikki Woffenden",
  "publication_date": "2021-01-07",
  "genre": "romance",
  "publisher": "Lazzy",
  "num_pages": 172,
  "language": "Lithuanian",
  "rating": 3.9,
  "available": False
}, {
  "book_title": "eget congue eget semper rutrum nulla nunc purus phasellus in felis donec",
  "author": "Ladonna Drissell",
  "publication_date": "2008-02-13",
  "genre": "mystery",
  "publisher": "Babblestorm",
  "num_pages": 858,
  "language": "Polish",
  "rating": 2.4,
  "available": True
}, {
  "book_title": "eget nunc donec quis orci eget orci vehicula condimentum curabitur in libero ut massa volutpat convallis morbi odio odio elementum",
  "author": "Chevy Barrim",
  "publication_date": "2022-03-19",
  "genre": "fiction",
  "publisher": "Twitterbridge",
  "num_pages": 120,
  "language": "Romanian",
  "rating": 2.3,
  "available": True
}, {
  "book_title": "nisl venenatis lacinia aenean sit amet justo morbi ut odio cras mi pede malesuada in",
  "author": "Clifford Glauber",
  "publication_date": "2015-09-07",
  "genre": "romance",
  "publisher": "Lazz",
  "num_pages": 322,
  "language": "Zulu",
  "rating": 2.3,
  "available": True
}, {
  "book_title": "diam vitae quam suspendisse potenti nullam porttitor lacus at turpis donec posuere metus vitae ipsum aliquam non mauris morbi non",
  "author": "Melonie Douche",
  "publication_date": "2018-10-24",
  "genre": "non-fiction",
  "publisher": "Tagtune",
  "num_pages": 689,
  "language": "Kurdish",
  "rating": 3.5,
  "available": False
}, {
  "book_title": "ut massa quis augue luctus tincidunt nulla mollis molestie lorem quisque ut erat",
  "author": "Teddy Cammidge",
  "publication_date": "2010-01-05",
  "genre": "fiction",
  "publisher": "Aivee",
  "num_pages": 513,
  "language": "West Frisian",
  "rating": 2.2,
  "available": True
}, {
  "book_title": "tincidunt ante vel ipsum praesent blandit lacinia erat vestibulum sed magna at nunc commodo",
  "author": "Faustine Tomaskunas",
  "publication_date": "2008-03-11",
  "genre": "mystery",
  "publisher": "Gabvine",
  "num_pages": 976,
  "language": "Mongolian",
  "rating": 3.6,
  "available": False
}, {
  "book_title": "nulla pede ullamcorper augue a suscipit nulla elit ac nulla sed vel enim sit amet nunc viverra dapibus nulla suscipit",
  "author": "Brew Abrahamsen",
  "publication_date": "2009-09-29",
  "genre": "non-fiction",
  "publisher": "Mynte",
  "num_pages": 535,
  "language": "Kashmiri",
  "rating": 1.6,
  "available": True
}, {
  "book_title": "vestibulum aliquet ultrices erat tortor sollicitudin mi sit amet lobortis sapien",
  "author": "Chlo Satteford",
  "publication_date": "2016-05-13",
  "genre": "fiction",
  "publisher": "Brainsphere",
  "num_pages": 861,
  "language": "Haitian Creole",
  "rating": 4.6,
  "available": True
}, {
  "book_title": "elit proin risus praesent lectus vestibulum quam sapien varius ut",
  "author": "Manfred Wallman",
  "publication_date": "2011-11-21",
  "genre": "fiction",
  "publisher": "Mybuzz",
  "num_pages": 817,
  "language": "Burmese",
  "rating": 3.2,
  "available": False
}, {
  "book_title": "odio cras mi pede malesuada in imperdiet et commodo vulputate justo in blandit ultrices enim lorem ipsum dolor sit amet",
  "author": "Cinda Le Leu",
  "publication_date": "2007-07-07",
  "genre": "romance",
  "publisher": "Divape",
  "num_pages": 414,
  "language": "Mongolian",
  "rating": 4.2,
  "available": False
}, {
  "book_title": "tempus vivamus in felis eu sapien cursus vestibulum proin eu mi nulla ac enim in tempor turpis nec",
  "author": "Elaina Rottcher",
  "publication_date": "2012-10-27",
  "genre": "non-fiction",
  "publisher": "Midel",
  "num_pages": 236,
  "language": "Kazakh",
  "rating": 2.7,
  "available": True
}, {
  "book_title": "orci luctus et ultrices posuere cubilia curae nulla dapibus dolor vel est donec odio justo sollicitudin ut suscipit a",
  "author": "Kirby MacKeogh",
  "publication_date": "2017-04-29",
  "genre": "mystery",
  "publisher": "Oloo",
  "num_pages": 404,
  "language": "Kashmiri",
  "rating": 1.3,
  "available": True
}, {
  "book_title": "justo aliquam quis turpis eget elit sodales scelerisque mauris sit amet eros suspendisse accumsan tortor",
  "author": "Rainer Kremer",
  "publication_date": "2004-11-01",
  "genre": "romance",
  "publisher": "Devpoint",
  "num_pages": 792,
  "language": "West Frisian",
  "rating": 2.4,
  "available": False
}, {
  "book_title": "vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae donec pharetra magna vestibulum",
  "author": "Loleta Dimitriou",
  "publication_date": "2003-07-07",
  "genre": "romance",
  "publisher": "Bubblemix",
  "num_pages": 722,
  "language": "Danish",
  "rating": 3.0,
  "available": True
}, {
  "book_title": "cursus id turpis integer aliquet massa id lobortis convallis tortor risus dapibus augue vel accumsan tellus",
  "author": "Bobby McCudden",
  "publication_date": "2017-09-30",
  "genre": "romance",
  "publisher": "Fivechat",
  "num_pages": 657,
  "language": "Spanish",
  "rating": 2.7,
  "available": True
}, {
  "book_title": "donec vitae nisi nam ultrices libero non mattis pulvinar nulla pede ullamcorper augue",
  "author": "Read Throughton",
  "publication_date": "2022-07-23",
  "genre": "mystery",
  "publisher": "Quinu",
  "num_pages": 852,
  "language": "Malayalam",
  "rating": 1.2,
  "available": False
}, {
  "book_title": "at nulla suspendisse potenti cras in purus eu magna vulputate",
  "author": "Donny Yakushkev",
  "publication_date": "2002-11-01",
  "genre": "mystery",
  "publisher": "Yakidoo",
  "num_pages": 338,
  "language": "Azeri",
  "rating": 5.0,
  "available": False
}, {
  "book_title": "praesent lectus vestibulum quam sapien varius ut blandit non interdum",
  "author": "Lottie Girling",
  "publication_date": "2010-04-16",
  "genre": "mystery",
  "publisher": "Janyx",
  "num_pages": 208,
  "language": "Dhivehi",
  "rating": 3.0,
  "available": False
}, {
  "book_title": "tincidunt lacus at velit vivamus vel nulla eget eros elementum",
  "author": "Avivah Tran",
  "publication_date": "2014-10-16",
  "genre": "mystery",
  "publisher": "Jayo",
  "num_pages": 836,
  "language": "Hindi",
  "rating": 2.2,
  "available": True
}, {
  "book_title": "lacinia aenean sit amet justo morbi ut odio cras mi pede malesuada in imperdiet et commodo vulputate justo in blandit",
  "author": "Madella Weldon",
  "publication_date": "2006-11-25",
  "genre": "non-fiction",
  "publisher": "Twitterworks",
  "num_pages": 696,
  "language": "Chinese",
  "rating": 3.0,
  "available": True
}, {
  "book_title": "libero nam dui proin leo odio porttitor id consequat in consequat ut nulla sed accumsan felis ut at",
  "author": "Dolli Drohun",
  "publication_date": "2017-01-22",
  "genre": "fiction",
  "publisher": "Quamba",
  "num_pages": 986,
  "language": "Latvian",
  "rating": 1.1,
  "available": False
}, {
  "book_title": "felis eu sapien cursus vestibulum proin eu mi nulla ac enim in tempor turpis nec",
  "author": "Ermanno Como",
  "publication_date": "2001-11-14",
  "genre": "non-fiction",
  "publisher": "Skibox",
  "num_pages": 463,
  "language": "Czech",
  "rating": 2.8,
  "available": True
}, {
  "book_title": "praesent lectus vestibulum quam sapien varius ut blandit non interdum in ante vestibulum ante ipsum primis in faucibus",
  "author": "Chryste Vedishchev",
  "publication_date": "2005-01-02",
  "genre": "fiction",
  "publisher": "Edgeblab",
  "num_pages": 823,
  "language": "Tetum",
  "rating": 2.2,
  "available": False
}, {
  "book_title": "primis in faucibus orci luctus et ultrices posuere cubilia curae nulla",
  "author": "Artemas Edmans",
  "publication_date": "2012-01-02",
  "genre": "romance",
  "publisher": "Kamba",
  "num_pages": 771,
  "language": "Azeri",
  "rating": 1.7,
  "available": True
}, {
  "book_title": "accumsan felis ut at dolor quis odio consequat varius integer ac leo",
  "author": "Merrie Hullot",
  "publication_date": "2004-07-25",
  "genre": "romance",
  "publisher": "Yabox",
  "num_pages": 791,
  "language": "Filipino",
  "rating": 2.4,
  "available": False
}, {
  "book_title": "eget eros elementum pellentesque quisque porta volutpat erat quisque erat eros viverra eget congue",
  "author": "Vikki Follitt",
  "publication_date": "2007-05-23",
  "genre": "fiction",
  "publisher": "Aibox",
  "num_pages": 665,
  "language": "Tswana",
  "rating": 2.2,
  "available": True
}, {
  "book_title": "et ultrices posuere cubilia curae donec pharetra magna vestibulum aliquet",
  "author": "Susie Feehery",
  "publication_date": "2010-12-31",
  "genre": "non-fiction",
  "publisher": "Photolist",
  "num_pages": 903,
  "language": "Bengali",
  "rating": 1.6,
  "available": True
}, {
  "book_title": "et tempus semper est quam pharetra magna ac consequat metus sapien ut nunc vestibulum",
  "author": "Katy Chatenet",
  "publication_date": "2022-10-19",
  "genre": "fiction",
  "publisher": "Photobug",
  "num_pages": 702,
  "language": "Icelandic",
  "rating": 1.2,
  "available": False
}, {
  "book_title": "praesent blandit lacinia erat vestibulum sed magna at nunc commodo placerat praesent blandit nam nulla integer pede justo lacinia eget",
  "author": "Ingemar Robberecht",
  "publication_date": "2009-11-08",
  "genre": "romance",
  "publisher": "Myworks",
  "num_pages": 420,
  "language": "Dzongkha",
  "rating": 4.2,
  "available": True
}, {
  "book_title": "viverra eget congue eget semper rutrum nulla nunc purus phasellus in felis donec semper",
  "author": "Shoshana Aireton",
  "publication_date": "2012-02-06",
  "genre": "non-fiction",
  "publisher": "Rooxo",
  "num_pages": 243,
  "language": "Ndebele",
  "rating": 3.7,
  "available": False
}, {
  "book_title": "enim leo rhoncus sed vestibulum sit amet cursus id turpis integer aliquet massa",
  "author": "Alameda Witherington",
  "publication_date": "2022-09-02",
  "genre": "mystery",
  "publisher": "Gabtune",
  "num_pages": 951,
  "language": "Lithuanian",
  "rating": 3.8,
  "available": False
}, {
  "book_title": "mauris viverra diam vitae quam suspendisse potenti nullam porttitor lacus at turpis",
  "author": "Rodolfo Tollow",
  "publication_date": "2015-07-28",
  "genre": "romance",
  "publisher": "Devbug",
  "num_pages": 594,
  "language": "Gujarati",
  "rating": 4.7,
  "available": False
}, {
  "book_title": "maecenas pulvinar lobortis est phasellus sit amet erat nulla tempus vivamus in felis eu",
  "author": "Elana Hattam",
  "publication_date": "2019-05-20",
  "genre": "non-fiction",
  "publisher": "Yotz",
  "num_pages": 206,
  "language": "Icelandic",
  "rating": 2.6,
  "available": False
}, {
  "book_title": "eget massa tempor convallis nulla neque libero convallis eget eleifend luctus ultricies eu nibh quisque id justo sit amet sapien",
  "author": "Marjorie Belch",
  "publication_date": "2022-11-03",
  "genre": "romance",
  "publisher": "Ooba",
  "num_pages": 858,
  "language": "Estonian",
  "rating": 1.2,
  "available": True
}, {
  "book_title": "vivamus vestibulum sagittis sapien cum sociis natoque penatibus et magnis dis parturient montes nascetur ridiculus mus etiam vel",
  "author": "Vannie Keymar",
  "publication_date": "2000-11-19",
  "genre": "fiction",
  "publisher": "Talane",
  "num_pages": 572,
  "language": "New Zealand Sign Language",
  "rating": 3.5,
  "available": False
}, {
  "book_title": "varius nulla facilisi cras non velit nec nisi vulputate nonummy maecenas tincidunt lacus at velit vivamus vel",
  "author": "Falito Burlingham",
  "publication_date": "2005-04-27",
  "genre": "romance",
  "publisher": "Blognation",
  "num_pages": 528,
  "language": "Finnish",
  "rating": 1.6,
  "available": False
}, {
  "book_title": "eu mi nulla ac enim in tempor turpis nec euismod scelerisque quam turpis adipiscing lorem vitae mattis nibh",
  "author": "Hyacintha Theobald",
  "publication_date": "2020-12-17",
  "genre": "non-fiction",
  "publisher": "Babbleopia",
  "num_pages": 914,
  "language": "Mongolian",
  "rating": 4.7,
  "available": False
}, {
  "book_title": "mi sit amet lobortis sapien sapien non mi integer ac neque duis",
  "author": "Ursa Lange",
  "publication_date": "2014-01-05",
  "genre": "fiction",
  "publisher": "Quimm",
  "num_pages": 295,
  "language": "Danish",
  "rating": 3.9,
  "available": False
}, {
  "book_title": "sit amet nunc viverra dapibus nulla suscipit ligula in lacus",
  "author": "Doe Mendel",
  "publication_date": "2003-05-31",
  "genre": "mystery",
  "publisher": "Zava",
  "num_pages": 946,
  "language": "Nepali",
  "rating": 3.0,
  "available": True
}, {
  "book_title": "eleifend donec ut dolor morbi vel lectus in quam fringilla rhoncus mauris enim leo rhoncus sed",
  "author": "Katina Pennazzi",
  "publication_date": "2006-04-30",
  "genre": "romance",
  "publisher": "Jabberstorm",
  "num_pages": 29,
  "language": "Nepali",
  "rating": 4.0,
  "available": True
}, {
  "book_title": "vestibulum sit amet cursus id turpis integer aliquet massa id",
  "author": "Traci Buckland",
  "publication_date": "2007-01-24",
  "genre": "non-fiction",
  "publisher": "Browsezoom",
  "num_pages": 629,
  "language": "Japanese",
  "rating": 4.6,
  "available": False
}, {
  "book_title": "curae nulla dapibus dolor vel est donec odio justo sollicitudin ut suscipit a feugiat et",
  "author": "Flor Eveleigh",
  "publication_date": "2002-02-15",
  "genre": "fiction",
  "publisher": "Lazzy",
  "num_pages": 139,
  "language": "Macedonian",
  "rating": 3.6,
  "available": True
}, {
  "book_title": "mattis egestas metus aenean fermentum donec ut mauris eget massa tempor convallis nulla neque libero convallis eget eleifend luctus",
  "author": "Hortense Littlechild",
  "publication_date": "2016-07-15",
  "genre": "mystery",
  "publisher": "Tagfeed",
  "num_pages": 51,
  "language": "Norwegian",
  "rating": 1.5,
  "available": True
}, {
  "book_title": "volutpat eleifend donec ut dolor morbi vel lectus in quam fringilla rhoncus mauris enim leo rhoncus sed",
  "author": "Jacinda Hollow",
  "publication_date": "2006-12-27",
  "genre": "non-fiction",
  "publisher": "Jabbertype",
  "num_pages": 778,
  "language": "Swahili",
  "rating": 1.9,
  "available": False
}, {
  "book_title": "volutpat quam pede lobortis ligula sit amet eleifend pede libero quis orci nullam molestie nibh in lectus",
  "author": "Edythe Maulin",
  "publication_date": "2011-12-26",
  "genre": "non-fiction",
  "publisher": "Divape",
  "num_pages": 835,
  "language": "Aymara",
  "rating": 2.9,
  "available": False
}, {
  "book_title": "mauris eget massa tempor convallis nulla neque libero convallis eget eleifend luctus ultricies eu nibh quisque id justo sit amet",
  "author": "Trace Shutle",
  "publication_date": "2018-11-14",
  "genre": "non-fiction",
  "publisher": "Skilith",
  "num_pages": 399,
  "language": "Dhivehi",
  "rating": 4.0,
  "available": True
}, {
  "book_title": "vulputate justo in blandit ultrices enim lorem ipsum dolor sit amet consectetuer adipiscing elit proin interdum mauris non ligula pellentesque",
  "author": "Sharon Upcraft",
  "publication_date": "2016-09-25",
  "genre": "non-fiction",
  "publisher": "Skidoo",
  "num_pages": 353,
  "language": "Tswana",
  "rating": 3.3,
  "available": False
}, {
  "book_title": "erat tortor sollicitudin mi sit amet lobortis sapien sapien non mi integer ac neque duis bibendum",
  "author": "Adlai Benck",
  "publication_date": "2001-08-22",
  "genre": "fiction",
  "publisher": "Miboo",
  "num_pages": 909,
  "language": "Northern Sotho",
  "rating": 2.6,
  "available": True
}, {
  "book_title": "etiam justo etiam pretium iaculis justo in hac habitasse platea dictumst etiam faucibus cursus urna ut tellus nulla ut erat",
  "author": "Vale Ellesworthe",
  "publication_date": "2019-10-17",
  "genre": "romance",
  "publisher": "Divape",
  "num_pages": 409,
  "language": "Assamese",
  "rating": 3.8,
  "available": False
}, {
  "book_title": "at vulputate vitae nisl aenean lectus pellentesque eget nunc donec quis orci eget orci vehicula condimentum curabitur in libero",
  "author": "Jorrie Orpwood",
  "publication_date": "2019-03-12",
  "genre": "non-fiction",
  "publisher": "Oyope",
  "num_pages": 461,
  "language": "Croatian",
  "rating": 2.3,
  "available": False
}, {
  "book_title": "sit amet turpis elementum ligula vehicula consequat morbi a ipsum integer a nibh in quis justo maecenas",
  "author": "Vanya Fauning",
  "publication_date": "2002-02-28",
  "genre": "romance",
  "publisher": "Snaptags",
  "num_pages": 637,
  "language": "West Frisian",
  "rating": 3.4,
  "available": True
}, {
  "book_title": "ipsum dolor sit amet consectetuer adipiscing elit proin risus praesent lectus vestibulum",
  "author": "Bobbette Gudgen",
  "publication_date": "2000-03-05",
  "genre": "fiction",
  "publisher": "Trunyx",
  "num_pages": 834,
  "language": "Gagauz",
  "rating": 4.8,
  "available": True
}, {
  "book_title": "neque sapien placerat ante nulla justo aliquam quis turpis eget",
  "author": "Zonda Winwright",
  "publication_date": "2010-12-02",
  "genre": "non-fiction",
  "publisher": "Trunyx",
  "num_pages": 668,
  "language": "Kurdish",
  "rating": 1.2,
  "available": True
}, {
  "book_title": "urna pretium nisl ut volutpat sapien arcu sed augue aliquam erat volutpat in congue etiam justo etiam pretium iaculis",
  "author": "Paloma Losano",
  "publication_date": "2017-05-01",
  "genre": "non-fiction",
  "publisher": "Quaxo",
  "num_pages": 410,
  "language": "Quechua",
  "rating": 2.4,
  "available": False
}, {
  "book_title": "mauris sit amet eros suspendisse accumsan tortor quis turpis sed ante vivamus tortor duis",
  "author": "Giraldo Juleff",
  "publication_date": "2020-02-08",
  "genre": "romance",
  "publisher": "Brainbox",
  "num_pages": 151,
  "language": "Persian",
  "rating": 4.8,
  "available": True
}]

for data in book_data:
    book = Library(
        book_title=data["book_title"],
        author=data["author"],
        publication_date=data["publication_date"],
        genre=data["genre"],
        publisher=data["publisher"],
        num_pages=data["num_pages"],
        language=data["language"],
        rating=data["rating"],
        available=data["available"]
    )
    book.save()
