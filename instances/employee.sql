create table EMPLOYEE (
	employee_id SERIAL PRIMARY KEY NOT,
	store_id INT NOT NULL ,
	fullname VARCHAR(100) ,
	email VARCHAR(100) UNIQUE NOT NULL ,
	password VARCHAR(100) NOT NULL UNQIUE
);
insert into employee (store_id, fullname, email, password) values (1, 'Bert', 'biskowitz0@rakuten.co.jp', '$2a$04$15W.6iKsAOEhEHdGh0gaHOI6eavBeJUARuaFkqSVZien5hs4Gtkyu');
insert into employee (store_id, fullname, email, password) values (1, 'Vivia', 'vduddell1@indiatimes.com', '$2a$04$N59qFLm4VGuPqQT7r4yv8.2n5/IJ4AdT/ajPgpBz5j/pczDmoR2PO');
insert into employee (store_id, fullname, email, password) values (1, 'Adina', 'adunbar2@instagram.com', '$2a$04$7jw6aeCGCwpVC5l/ajffMOVzuoivhmRpAVxLs1zNwP8XTrCooApAu');
insert into employee (store_id, fullname, email, password) values (1, 'Joscelin', 'jwoodyer3@spiegel.de', '$2a$04$hLXbuaW5t3fbsMcEoTLTCu9fZNtk1SNjDR1SZh1dMiVmSThFL9kL2');
insert into employee (store_id, fullname, email, password) values (1, 'Cosetta', 'cpyzer4@bravesites.com', '$2a$04$8Al.uq9Sj3nbBvkzi96K/uKdcdf2m5SgGbfDQdbEfYhru9PFQmwd2');






-- insert into employee (store_id, fullname, email, password) values (1, 'Matilde', 'mchin5@blogs.com', '$2a$04$Khc2hjSm1qf/0.Xb0Y5f.uTlshTQPHFcAOGKt03gzIplIhrA86JUC');
-- insert into employee (store_id, fullname, email, password) values (1, 'Catherina', 'ccolbert6@sphinn.com', '$2a$04$bTwyY0jckn2GO5de/xVU2uKeuRQf0CQIIdMAP7dsbsQgGTQ6hY4FO');
-- insert into employee (store_id, fullname, email, password) values (1, 'Vannie', 'vmalham7@engadget.com', '$2a$04$TVGJyOSCd9xGcH4lwLHszeNz7f2LoloFdpiyDZU/VT/A6TaQr7e4K');
-- insert into employee (store_id, fullname, email, password) values (1, 'Sherm', 'sdennehy8@vimeo.com', '$2a$04$e2qGh/S7VTuqiDaoK1yhNuzgNBfh9tLK61g8sVghhyR.QdLrT39zW');
-- insert into employee (employee_id, store_id, fullname, email, password) values (10, 17, 'Veronike', 'vduffer9@state.gov', '$2a$04$dNuCKq.Wc94Dhzho.2FQH.J4paj/dR/7xx462TxmVGyLk4xbLXgSy');
-- insert into employee (employee_id, store_id, fullname, email, password) values (11, 4, 'Starla', 'sfrohocka@boston.com', '$2a$04$eLlprDI32E9IpRdLhQGOWuJEiTLWPIQHze6Oxw6pwXfqjgTfjJOOG');
-- insert into employee (employee_id, store_id, fullname, email, password) values (12, 5, 'Gerik', 'gpedlowb@geocities.jp', '$2a$04$KWTwH9../ia2UCwjmFujs.PTPkuoeN0zRvN81zFR.VZwi8ZDlf5.G');
-- insert into employee (employee_id, store_id, fullname, email, password) values (13, 20, 'Giordano', 'gtyddc@cornell.edu', '$2a$04$blQsRRWXgk9E3J9lsdyI2uEC.ksxPgSAbVCj4MQiPIACAE3NgUqYW');
-- insert into employee (employee_id, store_id, fullname, email, password) values (14, 10, 'Ronnie', 'rtallantd@woothemes.com', '$2a$04$f0geo5piNglwpHqygGwNVOidM2Z2.t4s65kNwDlTpPp8XkapEfak.');
-- insert into employee (employee_id, store_id, fullname, email, password) values (15, 3, 'Rosella', 'rjenkine@ted.com', '$2a$04$tsmpe/Pc67aaQjq0.aHtY.0vTdXLsvC8qw.WFYGhrp6la3lnlKP12');
-- insert into employee (employee_id, store_id, fullname, email, password) values (16, 13, 'Tomas', 'tbarmef@dailymail.co.uk', '$2a$04$Y0yQ.b5/9TkPHcRHHnxzTui912Me1C3AW5hiP5QvdOyxAwrwv7GlS');
-- insert into employee (employee_id, store_id, fullname, email, password) values (17, 6, 'Catharina', 'cespinozag@cdc.gov', '$2a$04$g7vLk46ZGoy85h.YscXeSeGn8v/qOuxhxgGb0qlPa6/OCVhYT4Zhu');
-- insert into employee (employee_id, store_id, fullname, email, password) values (18, 18, 'Dudley', 'dwesthoferh@yolasite.com', '$2a$04$546KLMgFS1jSbWFNlBvTAOjZ2uXZ9RdxhXof6B6BwdeiVtZ5hHZoG');
-- insert into employee (employee_id, store_id, fullname, email, password) values (19, 2, 'Nikkie', 'nreallyi@php.net', '$2a$04$sTI8FpBMwrQeXr4UAHt7OuO5TiAKPnvbKz7ZWtz3TqXxwXaf70ezW');
-- insert into employee (employee_id, store_id, fullname, email, password) values (20, 19, 'Harmonie', 'hpopescuj@ucla.edu', '$2a$04$V5XBW3BWDtowurQh6Ks6duP0Y8hg52C0.rIGz3PBVm59gpfx137qO');
-- insert into employee (employee_id, store_id, fullname, email, password) values (21, 9, 'Aloise', 'anegalk@redcross.org', '$2a$04$2/QwOqqj8zeaQ5yQATfqheHk6SwF8Wrio9HG75VYRrnrC.vmB3ywK');
-- insert into employee (employee_id, store_id, fullname, email, password) values (22, 8, 'Sella', 'sgeekiel@ucoz.com', '$2a$04$dI0mzrQFvq52Z3aRTtMaB.NxrTMsZmxWSgsZ7hoKw06kNmN00SIcC');
-- insert into employee (employee_id, store_id, fullname, email, password) values (23, 2, 'Roana', 'rizkoviczm@fastcompany.com', '$2a$04$/1WUg6C8Y4bmMKvGKufwVuI/cVM9YtZ1u7T/SSlBMkCigDw57gsr.');
-- insert into employee (employee_id, store_id, fullname, email, password) values (24, 14, 'Teodorico', 'tmilsonn@canalblog.com', '$2a$04$lz.V2Vaf5BGt/nrybNykHO3iMVV0.3cetpM8gCNWJutRDfEQX7nx2');
-- insert into employee (employee_id, store_id, fullname, email, password) values (25, 12, 'Bear', 'bhaggitho@newsvine.com', '$2a$04$sYJ7ETHv0qYZjvd/BKC7POQsHPzuBdTNcDcgBPaQQ9uyg21N0Tsja');
-- insert into employee (employee_id, store_id, fullname, email, password) values (26, 4, 'Cointon', 'ceselp@stanford.edu', '$2a$04$JctJkzY5446rsO1yPRkXtOPgtIXhiRO7BNNIi5M5OtHW0ysj1hI7W');
-- insert into employee (employee_id, store_id, fullname, email, password) values (27, 19, 'Dyana', 'dfidellq@amazon.co.uk', '$2a$04$tLxfdP6UdAcnwlrZJUQPyOZuGnlK4Uq/u5WffHcjZ6O7XHALo1lki');
-- insert into employee (employee_id, store_id, fullname, email, password) values (28, 17, 'Valera', 'vgrovehamr@bloglines.com', '$2a$04$ECuPNX9itDDsLoj5nemUceeDhhkM6zbSjJk.g1moUtVq7gYa1rZy2');
-- insert into employee (employee_id, store_id, fullname, email, password) values (29, 11, 'Ariel', 'ahenrichsens@cnn.com', '$2a$04$A08fbNHBIpXi5vexOx09kO.KGGHOPz1NzAfSeLrYcDc9o/8bKKPD2');
-- insert into employee (employee_id, store_id, fullname, email, password) values (30, 13, 'Gram', 'gdunstant@g.co', '$2a$04$e195B5VPBnPJq9xE5TpAie4AlaxJq1os7a59b9zIajI0DMkuJ8TUW');
-- insert into employee (employee_id, store_id, fullname, email, password) values (31, 16, 'Lacy', 'lelsdonu@smugmug.com', '$2a$04$JU0GO7qNpW6dGfKP7HNS4OGHcjWi7PtLeZLJh/Kxqd6jEI5taj1M6');
-- insert into employee (employee_id, store_id, fullname, email, password) values (32, 3, 'Samantha', 'sbalcockv@squidoo.com', '$2a$04$XWm4OM1AkCM2PTxyWSNlLeDKmoeHVayyVaWeno3Oe3hYZam8XVCzm');
-- insert into employee (employee_id, store_id, fullname, email, password) values (33, 1, 'Radcliffe', 'rbowgenw@odnoklassniki.ru', '$2a$04$Gaw1eyrDanzQOnHwwUX/Qea0IW.vuwlSlI1mvo1I9NBt0axGH1RcO');
-- insert into employee (employee_id, store_id, fullname, email, password) values (34, 5, 'Regen', 'rpaleyx@shop-pro.jp', '$2a$04$4ASCm5.3qq62V8b0AN3hiuzQ0306H/1hiHyi00uKkfw/mPIHoJduG');
-- insert into employee (employee_id, store_id, fullname, email, password) values (35, 7, 'Thea', 'tgratlandy@mapquest.com', '$2a$04$WI5rUxFZLdPRbMASvCFK8./f26K9KOwIp2ieBOSiP7iQKvKMo3j4C');
-- insert into employee (employee_id, store_id, fullname, email, password) values (36, 10, 'Annabel', 'acrathernz@angelfire.com', '$2a$04$R7SoIDwov9lN8hB6HyyiK.YCFJtHkaRqhBnXD6VvHzp3e6LaJmbDO');
-- insert into employee (employee_id, store_id, fullname, email, password) values (37, 6, 'Modesta', 'mwyld10@w3.org', '$2a$04$ClRbLmSx9wXzdvC0yXu.0uYeCsTI2zH/C8kjKinXeq8kN2FDtSDnC');
-- insert into employee (employee_id, store_id, fullname, email, password) values (38, 20, 'Pammy', 'pcornelissen11@imageshack.us', '$2a$04$HOMHy5fIldEgNluqPS2y1uCbZEcpKwZ8XpPxaGuehJiivaHU14UJm');
-- insert into employee (employee_id, store_id, fullname, email, password) values (39, 18, 'Guido', 'gposen12@disqus.com', '$2a$04$nn6fG4V9pfn9SAmahCAQse1vXLxtWkdv9B6P2xecv5AZyKwWW2Z6W');
-- insert into employee (employee_id, store_id, fullname, email, password) values (40, 15, 'Erin', 'elongstaff13@loc.gov', '$2a$04$Bpst9VtjOxGv6Zh9o4CiCuTM5LTLgbreoWF5pp8TNoZvIa/FzCVJS');
-- insert into employee (employee_id, store_id, fullname, email, password) values (41, 10, 'Syman', 'skassel14@gravatar.com', '$2a$04$UbRqmHFwLnWjbNJwx57OqOVytpAP0U3YRWvxhbV/AznWjsmuRQ9PG');
-- insert into employee (employee_id, store_id, fullname, email, password) values (42, 14, 'Hally', 'hfarncomb15@howstuffworks.com', '$2a$04$SMu.r2Qp7c4K1wlEiFrbrOypYt8ZH9oVc2XblRdUNx0ByADVqewgy');
-- insert into employee (employee_id, store_id, fullname, email, password) values (43, 12, 'Winny', 'wbaggott16@twitter.com', '$2a$04$brzD5wDdiiWONCnUMgqx/OiFV8Ls0WhwWwsX7V.wqgYr9tp8xhITu');
-- insert into employee (employee_id, store_id, fullname, email, password) values (44, 8, 'Sophronia', 'smcauliffe17@mozilla.org', '$2a$04$XV0zeJtGkGliNiv55qFBf.eE3thw4mxHRSVlHx/EZV9PhM0wQa0y2');
-- insert into employee (employee_id, store_id, fullname, email, password) values (45, 15, 'Jeremy', 'jskirven18@berkeley.edu', '$2a$04$UM0TKWz3etxGfSXbzLK.E.KQs57x2CcZH0Fbz0HUJmnY4t/THjDEu');
-- insert into employee (employee_id, store_id, fullname, email, password) values (46, 18, 'Jon', 'jconstanza19@constantcontact.com', '$2a$04$UGZRvEulMuzxe..m1ag0huVxKKEbqkgfg/uwVdB3E081ZqQfJuqwC');
-- insert into employee (employee_id, store_id, fullname, email, password) values (47, 2, 'Wheeler', 'wduggen1a@51.la', '$2a$04$084bzd4A2NlHu1K/LBDYm.rOsDH4BTmwtvbbN8JMTnao/LiBOtR6C');
-- insert into employee (employee_id, store_id, fullname, email, password) values (48, 9, 'Catharina', 'cpayne1b@vistaprint.com', '$2a$04$iEoksRD66i563I4RTEsmJ.xWcC5vf.vGdHIi3lpcecVjCEN.HreUG');
-- insert into employee (employee_id, store_id, fullname, email, password) values (49, 20, 'Bartel', 'bwhoolehan1c@flavors.me', '$2a$04$M9bjfQRj0vCc/kZdFYl07OiMvnZp1RIx5Co8yGy816nxcA3wqJQcy');
-- insert into employee (employee_id, store_id, fullname, email, password) values (50, 13, 'Sheppard', 'sabby1d@cisco.com', '$2a$04$w9lkQbXkE8bZmadaTsPE.uqWVSc6X1ylQlfwiagfZs9NOlPMGE51u');
-- insert into employee (employee_id, store_id, fullname, email, password) values (51, 19, 'Wallie', 'whazeley1e@omniture.com', '$2a$04$xyOPJ/mT4Gvm21/AMy5KUuYDZmIV1wM.0O5JGNECLC.FsKtlA3Xoi');
-- insert into employee (employee_id, store_id, fullname, email, password) values (52, 1, 'Ebeneser', 'ehasnney1f@patch.com', '$2a$04$AjLgYvR7zbtievFuu.TTy.LaqS3OtQnL7I3TvNaDl5PLjD/i9WYKO');
-- insert into employee (employee_id, store_id, fullname, email, password) values (53, 3, 'Townsend', 'tmenguy1g@artisteer.com', '$2a$04$kG4pi8kmsUxOvEbbGGFJouZY3ChtVo5TC.7.jGzLQkGfo6qm9lpEW');
-- insert into employee (employee_id, store_id, fullname, email, password) values (54, 4, 'Shea', 'ssancto1h@ocn.ne.jp', '$2a$04$qmy4hwyKOKik5Vgf1Wrm3Odvh4ewKxvYtHWy17X5MLTlH3gj5cCJu');
-- insert into employee (employee_id, store_id, fullname, email, password) values (55, 7, 'Guillaume', 'gyve1i@spotify.com', '$2a$04$Sfz4tvRDnWIFmlcv7wStl.OJUU53YCsaEUpBR0ZTYWdlqauGkfXSW');
-- insert into employee (employee_id, store_id, fullname, email, password) values (56, 17, 'Otha', 'oreynalds1j@tmall.com', '$2a$04$HQaj6MgeBaFnPXY3xTXf2uU1PJvgZSMQtTcqXx0eTqhFSOcM7CoRu');
-- insert into employee (employee_id, store_id, fullname, email, password) values (57, 5, 'Anne-marie', 'adyde1k@reuters.com', '$2a$04$fvwjKbjo3.bGgIL.3BFoF.VybvaEtEqijMRwrJsUSOyiuKFLxD6Ge');
-- insert into employee (employee_id, store_id, fullname, email, password) values (58, 6, 'Dedra', 'ddymoke1l@hatena.ne.jp', '$2a$04$6OtvRyw0.HlUZTzuHeikDeUebC1V86S74OSBsClk//dsQyPbN.7GK');
-- insert into employee (employee_id, store_id, fullname, email, password) values (59, 11, 'Tiffie', 'tcapstaff1m@theguardian.com', '$2a$04$UeN81W4IkKcHFga8fmVJ/eCWeA0Dsp4ZHhRkLmzsHXrLQLCtmNHaW');
-- insert into employee (employee_id, store_id, fullname, email, password) values (60, 16, 'Lexie', 'lpitchford1n@tripadvisor.com', '$2a$04$nnftDKwEKJC58IKSGMEsHeiwco7noDJAA3GXKaiVxVnBbj/43yqju');
-- insert into employee (employee_id, store_id, fullname, email, password) values (61, 8, 'Lilith', 'lcamfield1o@dell.com', '$2a$04$kotgEEl8s29crU4zRM3Q7.4QUFy.xJSeYUi3NpNRWrfw0ft9lkCci');
-- insert into employee (employee_id, store_id, fullname, email, password) values (62, 9, 'Desmund', 'dpinshon1p@hc360.com', '$2a$04$giOs/R7iRW9PDLtrjovHWOABczf.FilmJ/4fx/yIGUS.mj.IiEcTi');
-- insert into employee (employee_id, store_id, fullname, email, password) values (63, 17, 'Catharina', 'crengger1q@mit.edu', '$2a$04$7UYlbfSFjTaYBU4yl/Is3uW6Q6qdze93jfaSA6Xz/FFmkr6dJf1gm');
-- insert into employee (employee_id, store_id, fullname, email, password) values (64, 13, 'Danielle', 'dbushell1r@bluehost.com', '$2a$04$vWJ4CNc5dar6rGSkgkkajucqn8f4zn7.t.NKjrFVe3Dn06SqzDHXW');
-- insert into employee (employee_id, store_id, fullname, email, password) values (65, 12, 'Gertrudis', 'grapkins1s@prlog.org', '$2a$04$Rd0ow.jZAGTA/2DFrezOueH1XfJaPZK1DAmpMAkBElkCYURMVTKB2');
-- insert into employee (employee_id, store_id, fullname, email, password) values (66, 3, 'Em', 'erimer1t@sina.com.cn', '$2a$04$Cx6RlAQn0SOoA2Yor29hCuOp1d2Z2ipIUccgFdjGvcRkZmUbihvM2');
-- insert into employee (employee_id, store_id, fullname, email, password) values (67, 11, 'Natalina', 'njouanny1u@drupal.org', '$2a$04$304QLBjtPLaMQkzq5BQJ2OX29SFLeo.CaBc2ktQQTH1wBzJRqgjUG');
-- insert into employee (employee_id, store_id, fullname, email, password) values (68, 7, 'Jemie', 'jgeekie1v@a8.net', '$2a$04$Rh8jVOQJYKovgYhb6p/YcuTFNoeXMcJVZyzAEvL5xUeeoL10tgiBG');
-- insert into employee (employee_id, store_id, fullname, email, password) values (69, 20, 'Fae', 'fcrayker1w@irs.gov', '$2a$04$qTaZcOFd.yzeVOiUr3t8peb9eTKtR2FYoh302Ws14W1B5DdVe8YqO');
-- insert into employee (employee_id, store_id, fullname, email, password) values (70, 19, 'Violante', 'vmackessock1x@washingtonpost.com', '$2a$04$OdFekyMZdRG9iQsULIwOBeCNEGOhz1rGnsWVxmBtAu4dbgzkPQ9Ei');
-- insert into employee (employee_id, store_id, fullname, email, password) values (71, 6, 'Cherish', 'cstatham1y@nih.gov', '$2a$04$JFlVcg2wdckryw2da89QG.G.DgIrd7PrMwskO/P.LjZBmlYpG9tCC');
-- insert into employee (employee_id, store_id, fullname, email, password) values (72, 4, 'Andreas', 'ahinkens1z@gmpg.org', '$2a$04$h7BwI/pK3jMppViwEgMbD.Rp3QpB/2lFUF7.1tsKwWpFPaNGX1//G');
-- insert into employee (employee_id, store_id, fullname, email, password) values (73, 1, 'Cordey', 'clambshine20@hugedomains.com', '$2a$04$4wLX.RQnmlHqPzaoKkSTIOkm7ZXAk.Ev2o2MRF.u2NMioi7/n.zPy');
-- insert into employee (employee_id, store_id, fullname, email, password) values (74, 18, 'Noelani', 'nsauvan21@go.com', '$2a$04$GkXqa90vDS/RP3oYwDD3tOjszG8WOD.v11FVo2mai.N/svagnEtoW');
-- insert into employee (employee_id, store_id, fullname, email, password) values (75, 5, 'Kilian', 'kburnapp22@springer.com', '$2a$04$FO6e230ugA45Yzeu8KvvquGRmEFvJpsSuN1l7456kr.aUCNGpglwG');
-- insert into employee (employee_id, store_id, fullname, email, password) values (76, 16, 'Doris', 'dchislett23@cdbaby.com', '$2a$04$rXE6E4sW.rSr.KH7oTJXe.2XvHaa5bskawyDVoUuyK9VQlFd/WlhW');
-- insert into employee (employee_id, store_id, fullname, email, password) values (77, 14, 'Horatius', 'hflageul24@amazon.de', '$2a$04$pXYqmWid1cXnWHefJLRVg.W378S7ZUtQmOhe/8SDAIaV7oe4/W3Xq');
-- insert into employee (employee_id, store_id, fullname, email, password) values (78, 15, 'Tammy', 'tkendle25@globo.com', '$2a$04$nx0qcf5WT20Qu8aZSchoiuauLVE8tGFKmXsu31OHmXN212BTP/JVu');
-- insert into employee (employee_id, store_id, fullname, email, password) values (79, 10, 'Dulcinea', 'ddoumerque26@google.es', '$2a$04$moLqPC1NRs.7u9SYvUHCUerO0mKLP1tYZi0k4lN206jtd54QXDyc6');
-- insert into employee (employee_id, store_id, fullname, email, password) values (80, 2, 'Karrie', 'kallwell27@yellowpages.com', '$2a$04$2vAbauHfT.X9b0k3Lj4kceQf3Epq6FeU6xLXiHqXdq3pVOpX0Y84G');
-- insert into employee (employee_id, store_id, fullname, email, password) values (81, 17, 'Kelbee', 'kklemz28@dell.com', '$2a$04$5xrThWrhAXqSqzMRDAZBauHaWriZOOeURXTxexz8XQXsnCUJ.mMnO');
-- insert into employee (employee_id, store_id, fullname, email, password) values (82, 16, 'Giulietta', 'gsudell29@pcworld.com', '$2a$04$mCpxYqJ.cIaA3N9YIl8uUewYoSmM2/rzrvhg7p/Jo1R1KreJl253a');
-- insert into employee (employee_id, store_id, fullname, email, password) values (83, 6, 'Max', 'msemaine2a@weather.com', '$2a$04$USisRe9JiyQrudemfBxLqeaw6RLufjnbBvTT8IdZFI4pgSp5.ptuq');
-- insert into employee (employee_id, store_id, fullname, email, password) values (84, 11, 'Morse', 'megdal2b@hao123.com', '$2a$04$hx6/umsmD4EVis7LmqGFq.GdROMQGnIWHN2XIMrJ9HfeS285d3pmm');
-- insert into employee (employee_id, store_id, fullname, email, password) values (85, 20, 'Jaimie', 'jgronaver2c@harvard.edu', '$2a$04$F7.uK0XTkGS18ukRKWGbse6a54PJvX9CwMYN70Mz62iQJFLhqM6lC');
-- insert into employee (employee_id, store_id, fullname, email, password) values (86, 13, 'Fidole', 'fboschmann2d@google.cn', '$2a$04$REKFDp.ZxaBXVkKNDN9c0.1k9AZ05ixsZoq4rLWlavZIKJrIrDv1G');
-- insert into employee (employee_id, store_id, fullname, email, password) values (87, 12, 'Sidonnie', 'saspell2e@etsy.com', '$2a$04$vS6e2dpEstnmcsxkO9bNy.dBvzeQpfEqqWbH79PtnKuv2ZxfHQUw6');
-- insert into employee (employee_id, store_id, fullname, email, password) values (88, 15, 'Norton', 'nvertigan2f@paginegialle.it', '$2a$04$VLZn4nbDTc0eXFPzhm8Qm.VcZhgGKctpPO0sU4Q50iDM1Ir2fDtLG');
-- insert into employee (employee_id, store_id, fullname, email, password) values (89, 9, 'Kevin', 'kvaisey2g@csmonitor.com', '$2a$04$s3y/NHMzRdZJ/MT/grCm1Og5a6TM4jDu6XQH8nICv61B/adOfY2Xi');
-- insert into employee (employee_id, store_id, fullname, email, password) values (90, 19, 'Ben', 'bgrabbam2h@tamu.edu', '$2a$04$JqKZ1Ot0eFwyQLwKDWtsDOs1Pce9WqenbcBI00p6ak5rFELAsFXPu');
-- insert into employee (employee_id, store_id, fullname, email, password) values (91, 7, 'Missy', 'mgrimsell2i@livejournal.com', '$2a$04$9r2cWqPIlu.uWZrNcdC9eeVWfmH5sPaiGwpnBmfrcIy3vJNfVJ3tq');
-- insert into employee (employee_id, store_id, fullname, email, password) values (92, 10, 'Maximilianus', 'mlindsay2j@bizjournals.com', '$2a$04$PAB.SPQcBKtBuS6gOpUiBOE9z.SMPqB3KqjiX7abhQBtz0X0VMdi2');
-- insert into employee (employee_id, store_id, fullname, email, password) values (93, 4, 'Adriena', 'agravie2k@google.com.hk', '$2a$04$6Lj1A23NMTCvrJIkgQqa4u0Lwa7lMWIU0sYYEP0hbeuIXDnKYUKWK');
-- insert into employee (employee_id, store_id, fullname, email, password) values (94, 8, 'Haydon', 'hgothliff2l@newyorker.com', '$2a$04$7JOE/4JEhbYk28lVTIvHuOQbJbGsWfwH4hi.7Tfl5FCfXpSGSx8rG');
-- insert into employee (employee_id, store_id, fullname, email, password) values (95, 3, 'Doralyn', 'dseiler2m@t.co', '$2a$04$cEngNvPsDfmsVc8t7qM57On5XK4tovvcGH.95fm6AKMzhiQFZ4MOW');
-- insert into employee (employee_id, store_id, fullname, email, password) values (96, 2, 'Byron', 'blemon2n@newsvine.com', '$2a$04$Ihp32IZxDF/cbdh1MaCUeeJO/0EeltGTiAf5CJ3b4h8Rw.BXCX8mK');
-- insert into employee (employee_id, store_id, fullname, email, password) values (97, 5, 'Nessie', 'ndennison2o@sfgate.com', '$2a$04$KC9e4eFoZDf2k8Ze9F8BH.36kUYVH6lsE9JqXDrZZIKOn6rr6vv2i');
-- insert into employee (employee_id, store_id, fullname, email, password) values (98, 18, 'Lark', 'lgelardi2p@pbs.org', '$2a$04$kI1.nh1vjazn0QpOM9N6HuWRdiXG3e/s2qk0pL52vN3.ZwZkEIO9K');
-- insert into employee (employee_id, store_id, fullname, email, password) values (99, 1, 'Hugo', 'hturtle2q@unblog.fr', '$2a$04$SztO1TXfK/ObD0O6PZKrweOX4/Mjm0z2nDFiadlKMyrGmrYb6MVEa');
-- insert into employee (employee_id, store_id, fullname, email, password) values (100, 14, 'Wylie', 'withell2r@parallels.com', '$2a$04$w5UV.5V0iri/..VMwDzFcut5F9k3Td82.Mv9270g870hGC1EO2V8G');
