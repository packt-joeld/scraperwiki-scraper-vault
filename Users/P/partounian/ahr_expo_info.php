<?php

require 'scraperwiki/simple_html_dom.php'; 

    $venues = array(1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,32,33,34,35,37,38,39,40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,180,181,182,183,185,186,187,188,189,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,208,209,210,211,212,213,214,215,216,217,218,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,268,269,270,271,272,273,274,275,276,277,278,279,280,281,282,283,284,285,286,287,288,289,290,291,292,293,294,295,296,297,298,299,300,301,302,303,304,305,306,307,308,309,310,311,312,313,314,315,316,317,318,319,320,321,322,323,324,325,326,327,328,329,330,331,332,333,334,335,336,337,338,339,340,341,342,343,344,345,346,347,348,349,350,351,352,353,354,355,356,357,358,359,360,361,362,363,364,366,367,368,369,370,371,372,373,374,375,376,377,378,379,380,381,382,383,384,385,386,388,389,390,391,392,393,394,395,396,397,398,399,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,416,417,418,419,420,421,422,423,424,425,428,430,431,434,435,436,437,440,441,442,443,446,448,449,452,456,457,459,460,461,462,463,464,465,466,467,468,470,471,472,473,475,478,479,481,490,491,492,493,495,496,497,498,500,501,502,503,504,505,506,514,515,517,518,519,520,521,522,523,524,527,528,529,530,537,538,539,540,541,542,543,545,546,548,549,550,552,553,554,555,556,559,560,561,562,563,564,565,567,568,570,572,573,574,575,576,577,578,579,580,581,584,586,587,588,589,591,592,593,594,596,598,599,601,602,603,604,605,607,608,609,610,611,612,613,614,615,616,617,618,619,620,621,622,770,771,772,773,774,775,776,777,778,779,780,781,782,783,784,785,786,787,789,790,791,793,794,795,796,797,798,799,800,801,802,803,804,805,806,807,849,989,1005,1014,1021,1023,1024,1026,1028,1029,1132,1168,1190,1195,1202,1415,1416,1440,1447,1458,1459,1485,1507,1509,1581,1583,1654,1705,1706,1707,1708,1709,1710,1711,1712,1713,1714,1715,1716,1717,1718,1728,1768,1777,1780,1782,1784,1800,1810,1992,1998,2000,2007,2058,2080,2110,2114,2122,2146,2182,2183,2184,2185,2186,2187,2188,2189,2190,2191,2192,2193,2194,2195,2196,2197,2198,2199,2200,2201,2202,2203,2204,2205,2206,2207,2208,2209,2210,2211,2212,2213,2214,2215,2217,2218,2219,2220,2221,2222,2223,2224,2225,2226,2227,2228,2229,2230,2231,2232,2233,2234,2235,2236,2237,2238,2239,2240,2241,2242,2243,2244,2245,2246,2247,2248,2249,2363,2381,2401,2404,2458,2487,2491,2505,2590,2651,2683,2695,2767,2939,2967,3039,3040,3139,3280,3312,3347,3423,3424,3425,3429,3442,3449,3452,3457,3458,3502,3612,3615,3621,3622,3623,3624,4021,4224,4242,4249,4283,4358,4359,4360,4362,4364,4365,4366,4367,4368,4369,4375,4395,4399,4413,4415,4710,4759,4868,4903,4910,4911,4913,4923,4927,4933,4940,4942,4944,4946,4954,4961,4962,4966,4967,4968,4978,4984,4991,4992,5022,5033,5041,5044,5045,5113,5288,5289,5291,5335,5469,5470,5471,5472,5476,5505,5540,5542,5554,5558,5568,5572,5573,5574,5575,5576,5577,5578,5579,5580,5581,5582,5583,5584,5585,5586,5587,5588,5589,5590,5591,5592,5593,5594,5595,5596,5597,5598,5599,5600,5601,5602,5603,5604,5605,5606,5607,5608,5609,5610,5611,5612,5613,5614,5615,5616,5617,5618,5619,5620,5621,5622,5623,5624,5625,5626,5627,5628,5629,5630,5631,5632,5633,5634,5635,5636,5637,5638,5639,5640,5641,5642,5643,5644,5645,5646,5647,5648,5649,5650,5652,5653,5654,5655,5656,5657,5658,5659,5660,5661,5662,5663,5664,5665,5666,5668,5669,5845,5846,5851,5854,5875,5889,5898,5901,5904,5906,5907,5911,5913,5921,5939,5948,5952,5954,5958,6018,6023,6041,6042,6043,6044,6045,6046,6047,6052,6054,6057,6059,6061,6063,6065,6066,6068,6069,6073,6078,6079,6080,6082,6083,6084,6085,6086,6088,6089,6090,6093,6095,6098,6099,6100,6101,6120,6127,6147,6152,6170,6181,6195,6199,6205,6220,6224,6225,6227,6228,6229,6230,6232,6233,6235,6237,6238,6239,6240,6242,6243,6244,6245,6246,6248,6249,6250,6252,6261,6262,6266,6267,6269,6270,6271,6285,6286,6288,6289,6495,6496,6500,6522,6523,6524,6525,6526,6527,6528,6529,6530,6531,6532,6533,6534,6535,6543,6549,6550,6551,7141,7282,7314,7417,7420,7460,7511,7579,7586,7598,7599,7620,7621,7637,7641,7659,7660,7833,7835,7836,7901,7912,7924,7927,7971,7973,7983,7984,7985,7986,8006,8036,8077,8220,8271,8284,8301,8308,8389,8428,8508,8535,8558,8654,8709,8713,8792,8795,8800,8812,8859,9056,9059,9063,9129,9133,9178,9213,9233,9265,9305,9325,9338,9341,9571,9593,9598,9655,9656,9685,9686,9730,9742,9750,9767,9769,9776,9822,10080,10081,10106,10115,10154,10210,10273,10302,10337,10400,10414,10437,10665,10709,10710,10760,10804,10817,10819,10822,10858,10899,12067,12407,12481,12624,12690,12936,13084,13197,13301,13463,13478,13480,13546,14224,14225,14226,14227,14228,14229,14230,14231,14232,14233,14234,14235,14236,14237,14238,14239,14240,14241,14242,14243,14244,14245,14246,14247,14248,14249,14251,14252,14253,14254,14255,14256,14257,14259,14260,14261,14262,14263,14264,14265,14266,14267,14268,14269,14270,14272,14273,14274,14275,14276,14277,14278,14279,14280,14282,14283,14284,14285,14286,14287,14288,14289,14290,14291,14292,14293,14294,14295,14296,14297,14298,14299,14300,14301,14302,14303,14304,14305,14306,14307,14308,14309,14310,14311,14312,14313,14314,14315,14316,14317,14318,14319,14320,14321,14322,14323,14324,14325,14326,14327,14328,14329,14330,14331,14332,14333,14334,14335,14336,14337,14338,14339,14340,14341,14342,14343,14344,14345,14346,14347,14348,14349,14350,14351,14352,14353,14354,14355,14356,14357,14358,14359,14360,14361,14362,14363,14364,14365,14366,14367,14368,14369,14370,14371,14372,14373,14374,14375,14376,14377,14378,14379,14380,14381,14382,14383,14384,14385,14386,14387,14388,14389,14390,14391,14392,14393,14394,14395,14396,14397,14398,14399,14400,14401,14402,14403,14404,14405,14406,14407,14408,14409,14410,14411,14412,14413,14414,14415,14416,14418,14419,14420,14421,14422,14423,14424,14425,14426,14427,14428,14429,14430,14431,14432,14433,14434,14435,14436,14437,14438,14439,14440,14442,14443,14445,14446,14447,14448,14449,14450,14451,14452,14453,14454,14455,14456,14457,14458,14459,14460,14461,14462,14463,14464,14465,14466,14467,14468,14469,14470,14471,14472,14473,14474,14475,14476,14477,14478,14479,14480,14481,14482,14483,14484,14485,14486,14487,14488,14489,14490,14491,14492,14493,14494,14495,14496,14497,14498,14499,14500,14501,14502,14503,14504,14505,14506,14507,14508,14509,14510,14511,14512,14513,14514,14515,14516,14517,14518,14519,14520,14521,14522,14523,14524,14525,14526,14527,14528,14529,14530,14674,14750,14771,14774,14775,14781,14903,14906,14909,14912,14913,14914,14919,14926,14927,14928,14929,14930,14951,14956,14958,15042,15043,15046,15053,15060,15061,15063,15066,15069,15094,15095,15097,15098,15099,15104,15115,15119,15120,15125,15129,15130,15131,15132,15133,15138,15150,15154,15155,15157,15158,15524,15593,15708,15726,15739,16089,16091,16531,16666,16685,16717,16761,16765,17000,17001,17013,17015,17017,17307,17325,17329,17657,17658,17772,18124,18339,18394,18523);
//for ($i = 1; $i <= 1520; $i++) {
    
    //scrape the page for the $hrefs
    $alllist = scraperwiki::scrape('http://ahr13.mapyourshow.com/5_0/exhibitor_results.cfm?type=alpha&alpha=@');
    $html_list = str_get_html('$alllist');

    foreach ($html_list->find('table td.mys-elastic mys-left a') as $el) {           
        print $el->href . "\n";
    } 

    // HTML of final target site and converted to string
    $html_content = scraperwiki::scrape('http://ahr13.mapyourshow.com/'.$el);
    $html = str_get_html($html_content);
    //within the HTML, find the name of the entry
    $companyname = $html->find('td.mys-elastic mys-left a', 0);
    $boothnumber = $html->find('td.mys-left', 0);
    $address = $html->find('li[class="first last"]', 0);
    $city = $html->find('span[class="date-display-single"]', 0);
    $zipcode = $html->find('span[class="date-display-single"]', 0);
    $email = $html->find('span[class="date-display-single"]', 0);
    $website = $html->find('span[class="date-display-single"]', 0);
    $phone = $html->find('span[class="date-display-single"]', 0);
    $fax = $html->find('span[class="date-display-single"]', 0);
//}    
    //save the data
    scraperwiki::save(array("id"),array("id"=>$i, 
    'companyname' => $companyname->plaintext,
    'boothnumber' => $boothnumber->plaintext,
    'address' => $address->plaintext,
    'city' => $city->plaintext,
    'zipcode' => $zipcode->plaintext,
    'email' => $email->plaintext,
    'website' => $website->plaintext,
    'phone' => $phone->plaintext,
    'fax' => $fax->plaintext,

));
?>