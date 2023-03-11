pip install snscrape
import snscrape.modules.twitter as sntwitter
import pandas as pd
import json

query = 'from:elonmusk since:2023-02-15 until:2023-03-07'
limit = 1000

tweets = sntwitter.TwitterSearchScraper(query).get_items()

df = pd.DataFrame(columns=['Date','URL' ,'Tweet'])

for index, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
    if index > limit:
        break
    df2 = {'Date': tweet.date, 'URL': tweet.url, 'Tweet': tweet.rawContent}
    df = pd.concat([df, pd.DataFrame.from_records([df2])])

print(df)

df.to_csv('elonmusk.csv')


output:
  
         Date  \
0  2023-03-06 22:36:57+00:00   
0  2023-03-06 22:08:42+00:00   
0  2023-03-06 20:38:06+00:00   
0  2023-03-06 20:25:15+00:00   
0  2023-03-06 20:14:06+00:00   
..                       ...   
0  2023-02-15 01:31:44+00:00   
0  2023-02-15 01:18:25+00:00   
0  2023-02-15 00:43:45+00:00   
0  2023-02-15 00:37:24+00:00   
0  2023-02-15 00:31:59+00:00   

                                                  URL  \
0   https://twitter.com/elonmusk/status/1632872927...   
0   https://twitter.com/elonmusk/status/1632865818...   
0   https://twitter.com/elonmusk/status/1632843016...   
0   https://twitter.com/elonmusk/status/1632839781...   
0   https://twitter.com/elonmusk/status/1632836977...   
..                                                ...   
0   https://twitter.com/elonmusk/status/1625669153...   
0   https://twitter.com/elonmusk/status/1625665801...   
0   https://twitter.com/elonmusk/status/1625657077...   
0   https://twitter.com/elonmusk/status/1625655479...   
0   https://twitter.com/elonmusk/status/1625654117...   

                                                Tweet  
0   @ryanhallyall It is a major priority to enable...  
0   Accounts engaging in repeated, egregious weapo...  
0                  @cb_doge @TrungTPhan I was robbed!  
0   @micsolana If what they want are pretty pics &...  
0   @BillyM2k @micsolana Yup, they can dish it out...  
..                                                ...  
0                      Twitter pinned lists are great  
0             @cb_doge @alifarhat79 High mileage club  
0       @hikingskiing A lot has happened in ten years  
0   @YoungBudgeteer @Jarrad_Hicks @abidc @anotherc...  
0   @alifarhat79 Damn, that’s impressive bus driving!  

[542 rows x 3 columns]

Output --- from received CSV file
--------------------------


Date	URL	Tweet
2023-03-06 22:36:57+00:00	https://twitter.com/elonmusk/status/1632872927816302594	"@ryanhallyall It is a major priority to enable monetization by content creators! People need to make a living and prosper from their work.

We need to make it possible to upload the content in the first place. Thatâ€™s getting there."
2023-03-06 22:08:42+00:00	https://twitter.com/elonmusk/status/1632865818563293190	"Accounts engaging in repeated, egregious weaponization of DMCA on Twitter or encouraging weaponization of DMCA will receive temporary suspensions. 

That said, reasonable media takedown requests are, of course, appropriate and will always be supported."
2023-03-06 20:38:06+00:00	https://twitter.com/elonmusk/status/1632843016749699073	@cb_doge @TrungTPhan I was robbed!
2023-03-06 20:25:15+00:00	https://twitter.com/elonmusk/status/1632839781997588488	"@micsolana If what they want are pretty pics &amp; heart emojiâ€™s, I recommend Instagram. Itâ€™s great for that, please go there.

Instagram reminds me of Cloud Cuckoo Land. Everything seems super nice on the surface, but itâ€™s actually hell. 

https://t.co/sVhNlJ8TjL"
2023-03-06 20:14:06+00:00	https://twitter.com/elonmusk/status/1632836977274880000	@BillyM2k @micsolana Yup, they can dish it out, but they canâ€™t take it
2023-03-06 20:13:03+00:00	https://twitter.com/elonmusk/status/1632836710705909761	@andrew_lilico @DavidDeutschOxf In a case like that, definitely.
2023-03-06 19:36:53+00:00	https://twitter.com/elonmusk/status/1632827612434165760	@DrJBhattacharya @MarkChangizi ðŸ’¯
2023-03-06 19:36:31+00:00	https://twitter.com/elonmusk/status/1632827520193110019	@monitoringbias Interesting
2023-03-06 19:32:38+00:00	https://twitter.com/elonmusk/status/1632826539787145216	@greg_price11 !
2023-03-06 18:52:23+00:00	https://twitter.com/elonmusk/status/1632816412593905666	@dogeofficialceo @BillyM2k @LGElectronics Weâ€™re working on it!
2023-03-06 18:27:14+00:00	https://twitter.com/elonmusk/status/1632810081497513993	"@pmarca A small API change had massive ramifications. The code stack is extremely brittle for no good reason. 

Will ultimately need a complete rewrite."
2023-03-06 18:24:23+00:00	https://twitter.com/elonmusk/status/1632809364594606081	@DrJBhattacharya ðŸŽ¯
2023-03-06 17:39:30+00:00	https://twitter.com/elonmusk/status/1632798070940344322	@BillyM2k @dogeofficialceo True, my @LGElectronics screen great!
2023-03-06 17:37:18+00:00	https://twitter.com/elonmusk/status/1632797515417370625	@Rainmaker1973 @NightLights_AM Any account engaging in blackmail will be suspended. Yours will not.
2023-03-06 17:32:34+00:00	https://twitter.com/elonmusk/status/1632796324356579331	@bronwynwilliams Super concerning
2023-03-06 17:31:57+00:00	https://twitter.com/elonmusk/status/1632796171574886401	@TheRabbitHole84 New Twitter is the source of truth
2023-03-06 17:31:01+00:00	https://twitter.com/elonmusk/status/1632795933741129728	@jordanbpeterson Idiocracy is happening so fast
2023-03-06 17:28:54+00:00	https://twitter.com/elonmusk/status/1632795401030885378	@jordanbpeterson True
2023-03-06 17:23:22+00:00	https://twitter.com/elonmusk/status/1632794008060567552	@alx This platform is so brittle (sigh). Will be fixed shortly.
2023-03-06 17:22:15+00:00	https://twitter.com/elonmusk/status/1632793727788785664	@stillgray !!
2023-03-06 17:21:43+00:00	https://twitter.com/elonmusk/status/1632793594665881600	@ZubyMusic Civilization is going ðŸ¥œ
2023-03-06 17:21:13+00:00	https://twitter.com/elonmusk/status/1632793469507780610	@ZubyMusic ðŸ¤£
2023-03-06 17:20:17+00:00	https://twitter.com/elonmusk/status/1632793235226599425	@BillFOXLA This is crazy!
2023-03-06 17:19:16+00:00	https://twitter.com/elonmusk/status/1632792979684327425	@isabelleboemeke True ðŸ˜”
2023-03-06 17:17:36+00:00	https://twitter.com/elonmusk/status/1632792556864937985	@WallStreetSilv This is messed up and will not make a difference to climate!
2023-03-06 17:16:31+00:00	https://twitter.com/elonmusk/status/1632792287372517377	@CollinRugg Good point. If an organization portrays itself as balanced, but is not, it should be labeled to inform the public.
2023-03-06 17:14:21+00:00	https://twitter.com/elonmusk/status/1632791740720488449	@DrJBhattacharya Exactly. Fauci egregiously betrayed the public trust.
2023-03-06 17:00:04+00:00	https://twitter.com/elonmusk/status/1632788147573497856	@FoxNews This is extremely unfair to anyone with XX chromosomes!
2023-03-06 11:36:09+00:00	https://twitter.com/elonmusk/status/1632706630927130627	@Annie_DLV True, have to admit trolls are kinda fun
2023-03-06 10:10:43+00:00	https://twitter.com/elonmusk/status/1632685129498869763	"@Chesschick01 Exactly. 

At the same time, worth noting that the left is not being censored either. 

This is not a right wing takeover, but rather a centrist takeover."
2023-03-06 10:06:05+00:00	https://twitter.com/elonmusk/status/1632683965902356483	@teslaownersSV Insane snow!
2023-03-06 10:04:14+00:00	https://twitter.com/elonmusk/status/1632683497574871041	@teslaownersSV Exactly
2023-03-06 09:59:54+00:00	https://twitter.com/elonmusk/status/1632682409366781953	(real article from organization calling itself bbc)
2023-03-06 09:57:26+00:00	https://twitter.com/elonmusk/status/1632681788941139972	Sorry for turning Twitter from nurturing paradise into place that has â€¦ trolls ðŸ§Œ https://t.co/HaWl1jPfOm
2023-03-06 08:40:37+00:00	https://twitter.com/elonmusk/status/1632662453950595072	@Rainmaker1973 A practical limit to digits of pi is how many are needed to divide the universe into Planck voxels
2023-03-06 08:36:59+00:00	https://twitter.com/elonmusk/status/1632661540645093377	@Rainmaker1973 This is arguably the most mind-blowing thing about â€œrealityâ€
2023-03-06 08:34:42+00:00	https://twitter.com/elonmusk/status/1632660967006806016	@WallStreetSilv Especially accurately â€¦ must be a tiny scale
2023-03-06 07:54:05+00:00	https://twitter.com/elonmusk/status/1632650743659331584	@WallStreetSilv Canâ€™t be an easy job weighing mice nuts
2023-03-06 07:27:49+00:00	https://twitter.com/elonmusk/status/1632644133868142592	@BillyM2k @BBCWorld Literally roflmao â€¦
2023-03-06 07:26:54+00:00	https://twitter.com/elonmusk/status/1632643904548880384	@BillyM2k @CommunityNotes Major asset on the side of truth &amp; accuracy!
2023-03-06 07:24:12+00:00	https://twitter.com/elonmusk/status/1632643223456829440	@BillyM2k @olivia_p_walker @CommunityNotes ðŸ¤£ðŸ’¯
2023-03-06 03:05:50+00:00	https://twitter.com/elonmusk/status/1632578205000384520	@anammostarac ðŸ¥‡
2023-03-06 02:51:51+00:00	https://twitter.com/elonmusk/status/1632574686851739648	@unusual_whales BI
2023-03-06 02:49:29+00:00	https://twitter.com/elonmusk/status/1632574090216103937	https://t.co/Qo6K6E1KkY
2023-03-05 23:35:58+00:00	https://twitter.com/elonmusk/status/1632525389863034882	@kimbal It is inspiring to think that humans did that
2023-03-05 23:35:15+00:00	https://twitter.com/elonmusk/status/1632525209503928322	@chicago_glenn The meme community has high standards!
2023-03-05 23:34:18+00:00	https://twitter.com/elonmusk/status/1632524972588695553	@ThePrimeagen As an attachment? How many chars? We are extending longform tweets to 10k soon.
2023-03-05 23:32:11+00:00	https://twitter.com/elonmusk/status/1632524437227716608	Add Fun to the FDA &amp; rename to FFDA
2023-03-05 23:30:06+00:00	https://twitter.com/elonmusk/status/1632523912893575168	@BillyM2k @POTUS What about fun? I say vote for more fun!
2023-03-05 22:56:26+00:00	https://twitter.com/elonmusk/status/1632515440692846593	@BBCNews !
2023-03-05 22:18:24+00:00	https://twitter.com/elonmusk/status/1632505870482300930	@dogeofficialceo @cb_doge ðŸ˜‚
2023-03-05 21:14:17+00:00	https://twitter.com/elonmusk/status/1632489736316018696	@DailyCaller Backlash the backlash, I say!!
2023-03-05 21:10:49+00:00	https://twitter.com/elonmusk/status/1632488861895884800	@the_wilderless ðŸ¥°
2023-03-05 21:04:45+00:00	https://twitter.com/elonmusk/status/1632487333491613696	@WhaleCoinTalk ðŸ‘€
2023-03-05 19:52:31+00:00	https://twitter.com/elonmusk/status/1632469158909575172	@BillyM2k @christinebarnum https://t.co/C9CG2GHlWg
2023-03-05 19:47:00+00:00	https://twitter.com/elonmusk/status/1632467767289954310	@BillyM2k @kevinolearytv I endorse this message!
2023-03-05 13:09:10+00:00	https://twitter.com/elonmusk/status/1632367650553618433	@DrJBhattacharya Rule #1: Donâ€™t panic
2023-03-05 13:06:24+00:00	https://twitter.com/elonmusk/status/1632366953766567936	@pmarca As the old saying goes: people in nuclear houses shouldnâ€™t glass each other
2023-03-05 12:53:38+00:00	https://twitter.com/elonmusk/status/1632363742749966337	@cb_doge ~8 years of pain from a crushed disc
2023-03-05 12:48:23+00:00	https://twitter.com/elonmusk/status/1632362420642410498	@DavidSacks @lieven_anatol I find myself, once again, in the odd position of agreeing with @jacobin
2023-03-05 07:03:54+00:00	https://twitter.com/elonmusk/status/1632275726912110593	How to sabotage an organization â€¦ https://t.co/YWtfgfRKCu
2023-03-05 03:08:07+00:00	https://twitter.com/elonmusk/status/1632216391880265728	@ashleevance @Peter_J_Beck Lot to be learned from buying old rocket parts &amp; especially by visiting museums like @airandspace &amp; @NASAKennedy rocket garden https://t.co/i3c0B5dsEU
2023-03-05 01:08:23+00:00	https://twitter.com/elonmusk/status/1632186257659838467	@pmarca People who throw the disinformation word around constantly are almost certainly guilty of engaging in it
2023-03-05 01:04:55+00:00	https://twitter.com/elonmusk/status/1632185385689161729	@westcoastbill Hard buttons did make my thumbs hurt from too much typing though
2023-03-05 01:03:21+00:00	https://twitter.com/elonmusk/status/1632184992779444226	Aiming to roll out ability to reply to individual DMs, use any reaction emoji &amp; encryption later this month
2023-03-04 20:20:13+00:00	https://twitter.com/elonmusk/status/1632113740807061504	@Resist_05 Iâ€™m super pro climate, but we definitely donâ€™t need to put farmers out of work to solve climate change. Not at all.
2023-03-04 20:10:05+00:00	https://twitter.com/elonmusk/status/1632111188153606147	https://t.co/Gegpl5sjHT
2023-03-04 20:09:57+00:00	https://twitter.com/elonmusk/status/1632111154498531328	@CatherinScience @ZubyMusic ðŸ¤£
2023-03-04 20:08:04+00:00	https://twitter.com/elonmusk/status/1632110681225920515	@DanielHadas2 ðŸ¤£
2023-03-04 20:03:18+00:00	https://twitter.com/elonmusk/status/1632109482305110017	@ZubyMusic But at least we give a megaphone
2023-03-04 20:02:36+00:00	https://twitter.com/elonmusk/status/1632109305846538241	@andst7 V true
2023-03-04 20:02:00+00:00	https://twitter.com/elonmusk/status/1632109154205675520	@paulg Terrible
2023-03-04 19:59:06+00:00	https://twitter.com/elonmusk/status/1632108425134981122	@Vegas And cool @boringcompany underground road tunnels!
2023-03-04 19:54:40+00:00	https://twitter.com/elonmusk/status/1632107309991067651	"@Rainmaker1973 Science found another ancient glyph
https://t.co/AIqUPy9Q2C"
2023-03-04 19:15:39+00:00	https://twitter.com/elonmusk/status/1632097491809181696	@BillyM2k @CommunityNotes ðŸ˜‚
2023-03-04 17:34:51+00:00	https://twitter.com/elonmusk/status/1632072126168440832	@ZubyMusic !!
2023-03-04 17:34:18+00:00	https://twitter.com/elonmusk/status/1632071986703921152	@mkapor @TheRealFreada @CommunityNotes Literally nothing is evenly distributed by zip code, except having a zip code
2023-03-04 17:18:10+00:00	https://twitter.com/elonmusk/status/1632067924390293504	@TheChiefNerd @rustyrockets @billmaher @joerogan Russell Brand is ðŸ”¥ðŸ”¥
2023-03-04 17:07:54+00:00	https://twitter.com/elonmusk/status/1632065341651054592	@andst7 ðŸ¤£
2023-03-04 17:05:32+00:00	https://twitter.com/elonmusk/status/1632064747964121090	"@mkapor @TheRealFreada What is your basis for claiming genius is evenly distributed by zip code? This is false.
@CommunityNotes"
2023-03-04 16:52:34+00:00	https://twitter.com/elonmusk/status/1632061483579330560	@BillyM2k @boardroom @MSU_Basketball @michiganstateu @Money23Green WoW
2023-03-04 16:48:05+00:00	https://twitter.com/elonmusk/status/1632060356930555904	We should defund the GEC
2023-03-04 16:40:00+00:00	https://twitter.com/elonmusk/status/1632058319144665088	@Rainmaker1973 17k rpm rotor â€“ wow
2023-03-04 13:56:23+00:00	https://twitter.com/elonmusk/status/1632017143498788867	Something should be done https://t.co/17mp4XdMI0
2023-03-04 13:51:29+00:00	https://twitter.com/elonmusk/status/1632015912927674368	@pmarca Very few Americans seem to realize the severity of the situation
2023-03-04 13:42:22+00:00	https://twitter.com/elonmusk/status/1632013616030334976	@ScottAdamsSays ðŸ”¥
2023-03-04 09:26:26+00:00	https://twitter.com/elonmusk/status/1631949208486912002	@paulg Not much useful originality with AI yet
2023-03-04 09:23:33+00:00	https://twitter.com/elonmusk/status/1631948483329503232	@BillyM2k Disturbing
2023-03-03 20:02:20+00:00	https://twitter.com/elonmusk/status/1631746850054352897	169 mT to orbit this year so far
2023-03-03 18:56:06+00:00	https://twitter.com/elonmusk/status/1631730183698001920	Stage 1 to stage 2 mass ratio is too high on Falcon 9, necessitating a long entry burn. This is fixed on Starship.
2023-03-03 18:39:00+00:00	https://twitter.com/elonmusk/status/1631725881378082816	Another launch
2023-03-03 18:16:10+00:00	https://twitter.com/elonmusk/status/1631720134636367872	â€œI used to be in crypto, but now I got interested in AI"
2023-03-03 17:20:09+00:00	https://twitter.com/elonmusk/status/1631706036292952064	@Cernovich @JackPosobiec That is the goal
2023-03-02 12:26:07+00:00	https://twitter.com/elonmusk/status/1631269653442961409	@Teslaconomics So many NNâ€™s, the visualizer tool crashes trying to render them
2023-03-02 11:38:33+00:00	https://twitter.com/elonmusk/status/1631257681473294338	@RichardDawkins This is insane
2023-03-02 07:59:49+00:00	https://twitter.com/elonmusk/status/1631202637184991237	@BillyM2k ðŸ¤£ðŸ’¯
2023-03-02 07:46:06+00:00	https://twitter.com/elonmusk/status/1631199184203182080	"The ability of Twitter advertising to reach the most influential people in the world is often not fully appreciated.

While a few other social networks are technically bigger, Twitter is where the writers &amp; leaders spend their time."
2023-03-02 07:27:08+00:00	https://twitter.com/elonmusk/status/1631194410552803328	@Teslaconomics Cybertruck cruisers will be next-level. Designed for Bladerunner.
2023-03-02 02:57:31+00:00	https://twitter.com/elonmusk/status/1631126559015747585	"Twice as many people died in Japan last year as were born. Population freefall.

Rest of the world is trending to follow.

https://t.co/JDHiFviua5"
2023-03-02 02:41:36+00:00	https://twitter.com/elonmusk/status/1631122553258274818	@FonsDK Exactly
2023-03-02 02:40:49+00:00	https://twitter.com/elonmusk/status/1631122359556947973	@lrocket Wow
2023-03-02 02:17:47+00:00	https://twitter.com/elonmusk/status/1631116559941771265	@kylegriffin1 Good for @LillyPad!
2023-03-01 23:57:05+00:00	https://twitter.com/elonmusk/status/1631081153024217091	@MKBHD Interesting
2023-03-01 22:41:29+00:00	https://twitter.com/elonmusk/status/1631062128147693573	@stevenmarkryan Bus voltage raised from 12V to 48V drops copper usage by ~4X
2023-03-01 22:35:51+00:00	https://twitter.com/elonmusk/status/1631060708715577348	@stevenmarkryan lol
2023-03-01 22:31:55+00:00	https://twitter.com/elonmusk/status/1631059721368076289	@ImMeme0 @KeithOlbermann @SenMikeLee @BasedMikeLee Olbermann posting from his dog account was epic
2023-03-01 22:16:01+00:00	https://twitter.com/elonmusk/status/1631055720153006080	Detailed whitepaper with calculations &amp; assumptions to be released by Tesla shortly
2023-03-01 22:14:04+00:00	https://twitter.com/elonmusk/status/1631055228089794560	https://t.co/PHv5nGLZGe
2023-03-01 22:06:37+00:00	https://twitter.com/elonmusk/status/1631053352200024064	@DavidSacks Accurate
2023-03-01 21:24:19+00:00	https://twitter.com/elonmusk/status/1631042709141037056	â€¦
2023-03-01 21:15:10+00:00	https://twitter.com/elonmusk/status/1631040406115823618	"Youâ€™re not gonna believe this, but weâ€™re running a little late! 

Presentation starts in ~5 mins."
2023-03-01 20:49:15+00:00	https://twitter.com/elonmusk/status/1631033881079197696	@quantumVerd @Twitter @Tesla obv
2023-03-01 20:47:08+00:00	https://twitter.com/elonmusk/status/1631033350746955777	@BillyM2k @Dexerto ðŸ˜‚
2023-03-01 20:45:10+00:00	https://twitter.com/elonmusk/status/1631032856616026112	@BillyM2k His best work imo
2023-03-01 20:37:28+00:00	https://twitter.com/elonmusk/status/1631030915810967552	@catturd2 His personal account (@BasedMikeLee) was incorrectly flagged as impersonation, which is not totally crazy, since it is based
2023-03-01 19:22:44+00:00	https://twitter.com/elonmusk/status/1631012111101972486	"@pmarca Once you acknowledge that alcohol is poison, itâ€™s fine to drink a little. The trade is a small amount of health for an even smaller amount of fun, but thatâ€™s not crazy to do once in a while with friends.

Alcohol is a legacy drug."
2023-03-01 07:15:08+00:00	https://twitter.com/elonmusk/status/1630829002112811009	@neontaster ðŸ”¥ðŸ”¥
2023-03-01 07:13:17+00:00	https://twitter.com/elonmusk/status/1630828537870524416	@Rainmaker1973 Intense
2023-03-01 07:08:42+00:00	https://twitter.com/elonmusk/status/1630827383602450432	@EvaFoxU ðŸ¤£
2023-03-01 07:00:06+00:00	https://twitter.com/elonmusk/status/1630825219429396480	@SawyerMerritt ðŸ¤£
2023-03-01 06:25:20+00:00	https://twitter.com/elonmusk/status/1630816472984330241	"What do you call an infinite gear ratio?
All torque, no action."
2023-03-01 00:13:28+00:00	https://twitter.com/elonmusk/status/1630722888448856070	@TeslaAIBot Photo filters are so misleading ðŸ¤£ðŸ¤£
2023-02-28 22:42:25+00:00	https://twitter.com/elonmusk/status/1630699974261370899	@WSJ @WSJopinion Good
2023-02-28 22:36:16+00:00	https://twitter.com/elonmusk/status/1630698427053899778	Periodic reminder to try using Twitter Lists. Will greatly improve your experience.
2023-02-28 21:23:19+00:00	https://twitter.com/elonmusk/status/1630680068417630214	@jamesdouma Accurate
2023-02-28 21:10:51+00:00	https://twitter.com/elonmusk/status/1630676928934952963	@Erdayastronaut Yeah
2023-02-28 19:54:53+00:00	https://twitter.com/elonmusk/status/1630657812530339855	@O42nl @kirillgroshkov Tesla does INT8 inference. Way more efficient than FP16, but took us a lot of effort to overcome quantization errors.
2023-02-28 19:51:19+00:00	https://twitter.com/elonmusk/status/1630656914466938881	@ajtourville @ulalaunch @SpaceX Wow, 9 years ago. Amazingly, the US was dependent on Russian engines for national security missions back then!
2023-02-28 19:42:59+00:00	https://twitter.com/elonmusk/status/1630654820565614593	"@Erdayastronaut Raptor start is now reliable on the test stand under most conditions. 

Now weâ€™re working on dynamically adapting the start sequence based on increasingly difficult propellant inlet pressures &amp; temps. 

Operating with low pressure, â€œwarmâ€ liquid oxygen is particularly important."
2023-02-28 19:33:17+00:00	https://twitter.com/elonmusk/status/1630652376087404554	@Tesmanian_com Kind words from @Toyota
2023-02-28 19:27:59+00:00	https://twitter.com/elonmusk/status/1630651042055462922	@Erdayastronaut Raptor start sequence is ðŸ¤¯ðŸ¤¯
2023-02-28 18:56:24+00:00	https://twitter.com/elonmusk/status/1630643095002857476	@ZubyMusic Looking into it
2023-02-28 18:44:20+00:00	https://twitter.com/elonmusk/status/1630640058507116553	https://t.co/4raodvAzSy
2023-02-28 18:14:42+00:00	https://twitter.com/elonmusk/status/1630632602913652756	@BillyM2k ðŸ¤£
2023-02-28 18:13:55+00:00	https://twitter.com/elonmusk/status/1630632405185843210	@AttilaTheLund You are right
2023-02-28 17:44:21+00:00	https://twitter.com/elonmusk/status/1630624962225553430	BasedAI
2023-02-28 16:51:15+00:00	https://twitter.com/elonmusk/status/1630611599370203138	@Not_the_Bee @TheBabylonBee !!
2023-02-28 16:48:51+00:00	https://twitter.com/elonmusk/status/1630610998460555264	@AlphaSignalAI Absolutely
2023-02-28 08:31:05+00:00	https://twitter.com/elonmusk/status/1630485729225703426	@Noahpinion We have made large construction projects almost illegal
2023-02-28 08:18:48+00:00	https://twitter.com/elonmusk/status/1630482637340004356	@cb_doge Anubis
2023-02-28 08:16:40+00:00	https://twitter.com/elonmusk/status/1630482099974070277	"@kkbaghel @McFaul Neither side has air superiority &amp; tanks are easily destroyed by missiles, so that leaves infantry &amp; artillery â€“ basically WW1. Drones are not yet available in sufficient numbers to matter, much like aircraft in WW1.

A defense in depth trench war means https://t.co/cQq2BHxPXtâ€¦ https://t.co/9ghdUP7iRi"
2023-02-28 07:52:38+00:00	https://twitter.com/elonmusk/status/1630476051670245376	"@McFaul Ukraine needs to be in max defense mode. Major Russian offensive coming.

Do you know how many casualties each side has taken?"
2023-02-28 07:45:28+00:00	https://twitter.com/elonmusk/status/1630474250569105411	@War_Mapper Almost surrounded
2023-02-28 07:17:48+00:00	https://twitter.com/elonmusk/status/1630467288720719873	@eightsleep Itâ€™s good
2023-02-28 06:34:38+00:00	https://twitter.com/elonmusk/status/1630456423153844224	@HeroDividend â€œBerkshire Hathaway high on Cokeâ€
2023-02-28 06:11:36+00:00	https://twitter.com/elonmusk/status/1630450625552044032	@cb_doge They forced me to buy it ðŸ¤£
2023-02-28 06:05:49+00:00	https://twitter.com/elonmusk/status/1630449172284420097	@mtracey Still no one is willing to articulate a realistic end game
2023-02-28 06:01:54+00:00	https://twitter.com/elonmusk/status/1630448186178273280	@YuqiiQian High time humanity built a permanently occupied base on the moon
2023-02-28 05:42:41+00:00	https://twitter.com/elonmusk/status/1630443351609573376	"@HistoryInPics If rendered to scale in that pic, the satellites would be smaller than a pixel, except maybe Space Station. 

Space is big. Real big."
2023-02-28 04:34:29+00:00	https://twitter.com/elonmusk/status/1630426188593217536	@BillFOXLA Only a small % is ever caught, which means the amount of fentanyl reaching consumers must be vastly greater
2023-02-28 04:19:02+00:00	https://twitter.com/elonmusk/status/1630422299034673153	@TrungTPhan @ashleevance â€œStinky Wifiâ€ is still my fav â€“ if you canâ€™t smell your wifi, how do you know itâ€™s real?
2023-02-28 04:15:45+00:00	https://twitter.com/elonmusk/status/1630421472027226112	@ashleevance Changing Starlink default wifi name to â€œFBI-vanâ€ on April 1
2023-02-28 04:12:15+00:00	https://twitter.com/elonmusk/status/1630420591856558080	@ashleevance ðŸ¤£
2023-02-28 03:12:55+00:00	https://twitter.com/elonmusk/status/1630405661677830147	@aaronjmate The diplomats want war and the warriors want peace
2023-02-28 03:08:39+00:00	https://twitter.com/elonmusk/status/1630404584748335104	@WholeMarsBlog Earth is almost entirely solar-powered already. Without the sun, weâ€™d just be a dark ice ball with some chemotrophic bacteria.
2023-02-28 02:40:02+00:00	https://twitter.com/elonmusk/status/1630397386290876417	@Lukewearechange True
2023-02-28 02:28:19+00:00	https://twitter.com/elonmusk/status/1630394434847227909	First Starlink v2 satellites reach orbit https://t.co/0l08568mJ9
2023-02-28 02:20:58+00:00	https://twitter.com/elonmusk/status/1630392586254053378	@lrocket The transition to argon was tricky, but necessary, as krypton is too rare
2023-02-28 01:41:12+00:00	https://twitter.com/elonmusk/status/1630382577113526274	@Erdayastronaut Propulsive landing FTW!
2023-02-27 20:13:28+00:00	https://twitter.com/elonmusk/status/1630300101594734593	"@JayCartere @ScottAdamsSays I donâ€™t agree with everything Scott says, but Dilbert is legit funny &amp; insightful.

We should stop canceling comedy!"
2023-02-27 20:08:06+00:00	https://twitter.com/elonmusk/status/1630298750202654720	@diana_dukic @catturd2 Accurate
2023-02-27 20:07:40+00:00	https://twitter.com/elonmusk/status/1630298644321648640	@WarlordDilley @catturd2 ðŸ¤£
2023-02-27 19:57:00+00:00	https://twitter.com/elonmusk/status/1630295958822043662	@catturd2 What about rightists admitting theyâ€™re wrong about being right? ðŸ¤”
2023-02-27 19:54:01+00:00	https://twitter.com/elonmusk/status/1630295206716227585	@dogeofficialceo ðŸ¤£ðŸ¤£
2023-02-27 19:52:50+00:00	https://twitter.com/elonmusk/status/1630294909751111681	@dogeofficialceo @DavidDeutschOxf ðŸ¤£
2023-02-27 19:50:34+00:00	https://twitter.com/elonmusk/status/1630294338398834690	"@DavidDeutschOxf Great way to understand to what degree one is wrong. 

We are all always at least a little bit wrong, but can aspire to be less so."
2023-02-27 19:16:17+00:00	https://twitter.com/elonmusk/status/1630285709654343683	https://t.co/IDVrLebj20
2023-02-27 18:59:34+00:00	https://twitter.com/elonmusk/status/1630281502603857921	@robbysoave @reason Very concerning
2023-02-27 17:10:56+00:00	https://twitter.com/elonmusk/status/1630254165690646528	@SciGuySpace Thatâ€™s roughly what they quoted SpaceX back then
2023-02-27 16:22:53+00:00	https://twitter.com/elonmusk/status/1630242072358952964	@Plinz ðŸ¤£
2023-02-27 16:22:36+00:00	https://twitter.com/elonmusk/status/1630242003609845761	@Jason ðŸ”¥ðŸ’¯
2023-02-27 15:00:38+00:00	https://twitter.com/elonmusk/status/1630221372902322178	@tesla_europe Great work!
2023-02-26 23:00:13+00:00	https://twitter.com/elonmusk/status/1629979679938543620	@DynamicWebPaige Haha true
2023-02-26 22:04:46+00:00	https://twitter.com/elonmusk/status/1629965724289495041	@BillyM2k @Jason @GeorgeTakei Haha true
2023-02-26 21:51:23+00:00	https://twitter.com/elonmusk/status/1629962353872715778	@saylor Not bad, SaylorGPT!
2023-02-26 21:49:48+00:00	https://twitter.com/elonmusk/status/1629961956227522563	@BillyM2k @greg16676935420 ðŸ¤£
2023-02-26 21:49:02+00:00	https://twitter.com/elonmusk/status/1629961762899361792	But, all things considered with regard to AGI existential angst, I would prefer to be alive now to witness AGI than be alive in the past and not
2023-02-26 21:42:38+00:00	https://twitter.com/elonmusk/status/1629960153414942721	@WallStreetSilv Wow
2023-02-26 21:36:07+00:00	https://twitter.com/elonmusk/status/1629958513051959299	@morgantepell ðŸ˜‚
2023-02-26 21:35:33+00:00	https://twitter.com/elonmusk/status/1629958369434796032	@emollick This answer is wrong. All fuel on CM is hypergolic, so dumping would prevent de-orbit burn &amp; atmospheric entry control.
2023-02-26 19:14:47+00:00	https://twitter.com/elonmusk/status/1629922947564486658	@fasc1nate ðŸ˜®
2023-02-26 19:09:46+00:00	https://twitter.com/elonmusk/status/1629921681547436035	@TheBabylonBee ðŸ˜‚
2023-02-26 19:00:09+00:00	https://twitter.com/elonmusk/status/1629919262105128962	@BillyM2k @WatcherGuru There will be a lot of robots
2023-02-26 18:58:32+00:00	https://twitter.com/elonmusk/status/1629918857967067149	@fasc1nate What if thatâ€™s just a tiny person?
2023-02-26 18:51:54+00:00	https://twitter.com/elonmusk/status/1629917188864761859	@DavidSacks So few know this
2023-02-26 18:51:42+00:00	https://twitter.com/elonmusk/status/1629917137396441092	@DavidSacks Exactly
2023-02-26 18:51:11+00:00	https://twitter.com/elonmusk/status/1629917006089666573	@Kristennetten AI+human vs AI+human is the next phase, but the human part will decrease in relevance over time, except perhaps as will, like our limbic system is to our cortex
2023-02-26 18:48:31+00:00	https://twitter.com/elonmusk/status/1629916335328165888	@LanceUlanoff Some
2023-02-26 18:48:10+00:00	https://twitter.com/elonmusk/status/1629916247063252993	@TheRabbitHole84 ðŸ¤£ðŸ¤£
2023-02-26 18:42:24+00:00	https://twitter.com/elonmusk/status/1629914794668048387	@KanekoaTheGreat He did it via a pass-through organization (EcoHealth)
2023-02-26 18:39:17+00:00	https://twitter.com/elonmusk/status/1629914011415244803	"Hope you have a good Sunday. 

First day of the rest of your life."
2023-02-26 18:37:32+00:00	https://twitter.com/elonmusk/status/1629913571151822849	@unusual_whales What!? No way.
2023-02-26 18:23:38+00:00	https://twitter.com/elonmusk/status/1629910072494026762	@howstuff_works Damn, that machine makes a lot of pretzels!
2023-02-26 18:11:35+00:00	https://twitter.com/elonmusk/status/1629907043220946946	@TheRabbitHole84 @BernieSanders Wow
2023-02-26 18:10:41+00:00	https://twitter.com/elonmusk/status/1629906815352799232	Astronaut launch for @NASA tomorrow night!
2023-02-26 17:55:05+00:00	https://twitter.com/elonmusk/status/1629902888423104513	@monitoringbias Absolutely
2023-02-26 17:51:22+00:00	https://twitter.com/elonmusk/status/1629901954234105857	Having a bit of AI existential angst today
2023-02-26 17:38:45+00:00	https://twitter.com/elonmusk/status/1629898777896026114	@monitoringbias Unfortunately, the elite colleges are teaching them this
2023-02-26 17:28:45+00:00	https://twitter.com/elonmusk/status/1629896262567772161	@CJFerguson1111 @monitoringbias Exactly
2023-02-26 17:19:14+00:00	https://twitter.com/elonmusk/status/1629893865783058434	@monitoringbias Very disproportionate to promote a false narrative
2023-02-26 17:18:06+00:00	https://twitter.com/elonmusk/status/1629893583548366856	@RampCapitalLLC ðŸ¤£
2023-02-26 17:17:05+00:00	https://twitter.com/elonmusk/status/1629893324860530697	@TheRabbitHole84 @WolfofLevittown @ScottAdamsSays Interesting
2023-02-26 17:13:20+00:00	https://twitter.com/elonmusk/status/1629892380697546754	@DavidSacks Accurate
2023-02-26 08:58:31+00:00	https://twitter.com/elonmusk/status/1629767858719793154	@ibuildthecloud lol
2023-02-26 08:45:38+00:00	https://twitter.com/elonmusk/status/1629764614870167552	"@monitoringbias For a *very* long time, US media was racist against non-white people, now theyâ€™re racist against whites &amp; Asians. 

Same thing happened with elite colleges &amp; high schools in America.

Maybe they can try not being racist."
2023-02-26 07:53:42+00:00	https://twitter.com/elonmusk/status/1629751544127037440	@monitoringbias The media is racist
2023-02-26 07:52:33+00:00	https://twitter.com/elonmusk/status/1629751256913682432	@MattWallace888 Back when I was ~$100k negative with student debt
2023-02-26 07:45:12+00:00	https://twitter.com/elonmusk/status/1629749405707382785	@robbystarbuck @EndWokeness !!
2023-02-26 07:43:51+00:00	https://twitter.com/elonmusk/status/1629749066383908865	@scienceisstrat1 Interesting
2023-02-26 07:41:25+00:00	https://twitter.com/elonmusk/status/1629748454925692932	@KanekoaTheGreat ðŸŽ¯
2023-02-26 07:40:59+00:00	https://twitter.com/elonmusk/status/1629748345148174336	@ImMeme0 @EndWokeness Maybe they donâ€™t realize that their propaganda is wrong?
2023-02-26 07:38:03+00:00	https://twitter.com/elonmusk/status/1629747606493581312	@Enezator ðŸ¤£
2023-02-26 07:33:33+00:00	https://twitter.com/elonmusk/status/1629746474496999427	@Jason So based. Nice work @nbcsnl!
2023-02-26 07:30:32+00:00	https://twitter.com/elonmusk/status/1629745715017596928	ðŸ¤¯
2023-02-26 07:29:23+00:00	https://twitter.com/elonmusk/status/1629745425631649793	@TheBabylonBee The Hangover is funny tho
2023-02-26 06:46:04+00:00	https://twitter.com/elonmusk/status/1629734523255545856	@nbcsnl Good one
2023-02-26 05:11:17+00:00	https://twitter.com/elonmusk/status/1629710671209193472	Rewatching Step Brothers â€¦ so good
2023-02-26 04:55:47+00:00	https://twitter.com/elonmusk/status/1629706771878096896	@Rainmaker1973 !
2023-02-26 04:49:49+00:00	https://twitter.com/elonmusk/status/1629705269033816064	ðŸ˜¢ https://t.co/3eGpfLlRQJ
2023-02-26 04:46:06+00:00	https://twitter.com/elonmusk/status/1629704334756724736	@GRDecter Accurate
2023-02-26 04:45:53+00:00	https://twitter.com/elonmusk/status/1629704278360178691	@AdultBroker1 @GRDecter There should be more product innovation at his companies tbh
2023-02-26 04:43:47+00:00	https://twitter.com/elonmusk/status/1629703751752724481	@TrungTPhan This thread is the best Doritos ad ever
2023-02-26 04:20:38+00:00	https://twitter.com/elonmusk/status/1629697927512768514	https://t.co/UAWjEyhe5U
2023-02-26 03:44:42+00:00	https://twitter.com/elonmusk/status/1629688882739527681	@adamdangelo ðŸ’¯
2023-02-26 03:39:49+00:00	https://twitter.com/elonmusk/status/1629687653229555716	Why canâ€™t witchcraft defeat inflation!?
2023-02-26 03:39:15+00:00	https://twitter.com/elonmusk/status/1629687510040281088	@pmarca That you follow so many people, but like so few tweets, confuses that heck out of our algorithm btw ðŸ¤£
2023-02-26 03:09:03+00:00	https://twitter.com/elonmusk/status/1629679910456262657	@EvaFoxU ðŸ¤£ðŸ’¯
2023-02-26 03:06:18+00:00	https://twitter.com/elonmusk/status/1629679220874985472	@pmarca ðŸ˜®
2023-02-26 02:44:29+00:00	https://twitter.com/elonmusk/status/1629673727360221184	@gurgavin Munger couldâ€™ve invested in Tesla at ~$200M valuation when I had lunch with him in late 2008
2023-02-26 02:41:50+00:00	https://twitter.com/elonmusk/status/1629673063175290880	@gurgavin Starts with a T â€¦
2023-02-26 02:39:07+00:00	https://twitter.com/elonmusk/status/1629672379097006080	@EvaFoxU @KanekoaTheGreat How did he get elected?
2023-02-26 02:16:14+00:00	https://twitter.com/elonmusk/status/1629666617473810432	@micsolana âšœï¸
2023-02-26 00:07:11+00:00	https://twitter.com/elonmusk/status/1629634142622334978	https://t.co/nBq4YHkaK4
2023-02-26 00:06:14+00:00	https://twitter.com/elonmusk/status/1629633902066425856	Disturbingly accurate
2023-02-26 00:04:58+00:00	https://twitter.com/elonmusk/status/1629633583626477568	@cb_doge @BillyM2k @JustinScerini ðŸ´â€â˜ ï¸
2023-02-26 00:04:10+00:00	https://twitter.com/elonmusk/status/1629633384338149378	https://t.co/OV8oI8vAIS
2023-02-26 00:02:28+00:00	https://twitter.com/elonmusk/status/1629632954900140034	@BillyM2k @JustinScerini Tumblr especially
2023-02-25 22:57:32+00:00	https://twitter.com/elonmusk/status/1629616613602254848	@DomitrosH @WholeMarsBlog lol true
2023-02-25 22:56:53+00:00	https://twitter.com/elonmusk/status/1629616451421192193	@WholeMarsBlog ðŸŽ¯
2023-02-25 22:34:19+00:00	https://twitter.com/elonmusk/status/1629610774053134339	@TrungTPhan ðŸ¤£
2023-02-25 22:33:24+00:00	https://twitter.com/elonmusk/status/1629610541051199495	@SmokeAwayyy Yikes
2023-02-25 22:31:30+00:00	https://twitter.com/elonmusk/status/1629610061847748609	@jordanbpeterson !!
2023-02-25 22:28:44+00:00	https://twitter.com/elonmusk/status/1629609366801244162	@teslaownersSV Doesnâ€™t seem real even when youâ€™re standing right next to it
2023-02-25 22:09:30+00:00	https://twitter.com/elonmusk/status/1629604528780713985	@rick_doobs ðŸ”¥
2023-02-25 22:08:33+00:00	https://twitter.com/elonmusk/status/1629604288384192514	@KanekoaTheGreat @DavidSacks Any to add or modify @CommunityNotes?
2023-02-25 21:49:11+00:00	https://twitter.com/elonmusk/status/1629599416251187202	@69dogecoin Deepfakes are getting so good I canâ€™t tell if this is real
2023-02-25 21:48:13+00:00	https://twitter.com/elonmusk/status/1629599169512890368	@69dogecoin Couldnâ€™t reach the toilet paper ðŸ˜¢
2023-02-25 21:45:13+00:00	https://twitter.com/elonmusk/status/1629598417159692288	https://t.co/5wIbOXFs1e
2023-02-25 21:44:10+00:00	https://twitter.com/elonmusk/status/1629598153010827264	@andst7 ðŸ¤£ðŸ¤£
2023-02-25 21:02:29+00:00	https://twitter.com/elonmusk/status/1629587662175629313	This meme is a for loop
2023-02-25 19:43:47+00:00	https://twitter.com/elonmusk/status/1629567857041260545	https://t.co/mMIaVMJsfY
2023-02-25 19:41:42+00:00	https://twitter.com/elonmusk/status/1629567331587493888	Roth IRA vs Wrath IRA
2023-02-25 19:37:12+00:00	https://twitter.com/elonmusk/status/1629566200064688129	But which is actually harder, defeating inflation or defeating the British â€¦ ?
2023-02-25 19:35:34+00:00	https://twitter.com/elonmusk/status/1629565786867081218	Inflation Reduction Act (IRA) vs Irish Republican Army (IRA) https://t.co/WKAftArwnW
2023-02-25 19:29:32+00:00	https://twitter.com/elonmusk/status/1629564271557328896	@billmaher Now is the time to fight the anti-human woke mind virus with everything!
2023-02-25 19:18:50+00:00	https://twitter.com/elonmusk/status/1629561576775712770	@IhloKapitan @prof_freedom ðŸ¤£
2023-02-25 19:10:29+00:00	https://twitter.com/elonmusk/status/1629559477404852227	@cb_doge @KrummAndreas @prof_freedom ðŸ¤£
2023-02-25 19:05:59+00:00	https://twitter.com/elonmusk/status/1629558344737341440	@KrummAndreas @prof_freedom Viking energy!
2023-02-25 19:04:54+00:00	https://twitter.com/elonmusk/status/1629558071214190592	@EVeerkamp @prof_freedom ðŸ¤£
2023-02-25 19:03:32+00:00	https://twitter.com/elonmusk/status/1629557727578955779	@mista98berk @prof_freedom ðŸ”¥
2023-02-25 18:41:59+00:00	https://twitter.com/elonmusk/status/1629552302381056000	@ScottAdamsSays Simultaneously, an interesting question and a tongue twister!
2023-02-25 18:38:02+00:00	https://twitter.com/elonmusk/status/1629551311149490179	@BillyM2k https://t.co/q3ciVDa3oM
2023-02-25 17:48:14+00:00	https://twitter.com/elonmusk/status/1629538776111280130	https://t.co/uRRapLN6S3
2023-02-25 17:37:27+00:00	https://twitter.com/elonmusk/status/1629536065164922880	https://t.co/I8f20JbkXu
2023-02-25 10:06:35+00:00	https://twitter.com/elonmusk/status/1629422599661842435	@ShitpostGate ðŸ¤£ðŸ¤£
2023-02-25 09:47:43+00:00	https://twitter.com/elonmusk/status/1629417851890159616	@KanekoaTheGreat That election was arguably dodgy, but no question that there was indeed a coup
2023-02-25 09:41:56+00:00	https://twitter.com/elonmusk/status/1629416397100011521	@KanekoaTheGreat @DavidSacks Accurate assessment by @DavidSacks
2023-02-25 09:34:35+00:00	https://twitter.com/elonmusk/status/1629414545570557954	@Tesmanian_com New metal
2023-02-25 01:03:15+00:00	https://twitter.com/elonmusk/status/1629285866223853570	@__SeriousGemini ðŸ˜‚
2023-02-25 01:02:35+00:00	https://twitter.com/elonmusk/status/1629285698879488000	@TheRabbitHole84 Kids were put in jail for this?
2023-02-25 00:54:18+00:00	https://twitter.com/elonmusk/status/1629283610413899779	"@Storm4Congress This idiotic algorithm change has been reverted. 

It also caused my account engagement to drop by a factor of ten, because it was based on absolute number of blocks, not blocks as a percentage of followers.

This meant any large account that posted anything â€œcontroversialâ€ wasâ€¦"
2023-02-25 00:06:13+00:00	https://twitter.com/elonmusk/status/1629271512841695235	@BillyM2k @dogeofficialceo !!!
2023-02-24 23:55:30+00:00	https://twitter.com/elonmusk/status/1629268816013213698	@dogeofficialceo This canâ€™t be real
2023-02-24 23:54:18+00:00	https://twitter.com/elonmusk/status/1629268513683652608	@ilove_aviation A380 looks like it already ate a few 737â€™s
2023-02-24 23:13:09+00:00	https://twitter.com/elonmusk/status/1629258158903271424	@BillyM2k @stillgray ðŸŽ¯
2023-02-24 22:47:08+00:00	https://twitter.com/elonmusk/status/1629251610135220226	"@RalphNader Ralph Nader, you are lying â€“ shame on you! I personally provided almost all Tesla funding, based on my proceeds from PayPal, from Series A in 2004 until Series C in 2007.

In late 2008, I gave Tesla the last money I had. It was that or the company would have died. We closed thatâ€¦"
2023-02-24 21:35:22+00:00	https://twitter.com/elonmusk/status/1629233548669452289	@kcoleman Cool
2023-02-24 21:08:36+00:00	https://twitter.com/elonmusk/status/1629226814299070464	@BillyM2k !!
2023-02-24 19:42:01+00:00	https://twitter.com/elonmusk/status/1629205021849010179	@Teslaconomics Death threats should result in immediate account suspension. Lmk if thatâ€™s not happening.
2023-02-24 19:31:24+00:00	https://twitter.com/elonmusk/status/1629202351637598208	@gunsnrosesgirl3 Stoic score 10/10
2023-02-24 19:30:24+00:00	https://twitter.com/elonmusk/status/1629202100369383425	@m0nick ðŸ¤£ðŸ¤£ Dad jokes ftw
2023-02-24 19:29:25+00:00	https://twitter.com/elonmusk/status/1629201852968452097	"I have unblocked everyone I blocked, apart from scammers. I recommend others do the same.

Negative feedback is a good thing."
2023-02-24 19:15:43+00:00	https://twitter.com/elonmusk/status/1629198406340976643	@WholeMarsBlog Ramping production (as always) will be the challenge, not demand
2023-02-24 18:12:21+00:00	https://twitter.com/elonmusk/status/1629182459236450312	@monitoringbias Disturbing
2023-02-24 17:51:27+00:00	https://twitter.com/elonmusk/status/1629177197238841354	@googlephotos Stalin wouldâ€™ve loved this feature https://t.co/cizT09xxty
2023-02-24 17:46:19+00:00	https://twitter.com/elonmusk/status/1629175906139877386	@adage @WPP Thatâ€™s great to hear!
2023-02-24 06:23:17+00:00	https://twitter.com/elonmusk/status/1629004015655690241	Space Elevator
2023-02-24 06:01:12+00:00	https://twitter.com/elonmusk/status/1628998457645047808	Check out my spicy ðŸŒ¶ï¸ ðŸ”¥ OnlyGANs!! https://t.co/b9lnJSEnvo
2023-02-24 05:46:49+00:00	https://twitter.com/elonmusk/status/1628994840665923584	@BillyM2k @TheUnderDoge3 ðŸ˜ 
2023-02-24 03:47:04+00:00	https://twitter.com/elonmusk/status/1628964700997267457	@derek_j_morris @pmarca Major problem
2023-02-24 03:35:43+00:00	https://twitter.com/elonmusk/status/1628961847364681731	@EvaFoxU Nice
2023-02-24 03:08:33+00:00	https://twitter.com/elonmusk/status/1628955011416743936	@DavidSacks A Russia-China alliance is inevitable. It will grow much stronger over time.
2023-02-23 22:05:41+00:00	https://twitter.com/elonmusk/status/1628878790616305664	@PeterDiamandis Yeah
2023-02-23 21:54:38+00:00	https://twitter.com/elonmusk/status/1628876008656105473	@lopatonok @UnderSecStateP Interesting thread
2023-02-23 20:44:25+00:00	https://twitter.com/elonmusk/status/1628858339907215360	@alx While there is relative good &amp; bad, there are no pure angels in war. Beware those who say they are.
2023-02-23 20:40:52+00:00	https://twitter.com/elonmusk/status/1628857446398832640	@growing_daniel ðŸ¤£
2023-02-23 19:53:19+00:00	https://twitter.com/elonmusk/status/1628845480628355073	"@KatiePavlich Maximum skill with monetary policy is extremely important in this role! 

A bad Fed decision affects the lives of everyone."
2023-02-23 19:43:41+00:00	https://twitter.com/elonmusk/status/1628843055586639873	@TheRabbitHole84 â™¥ï¸
2023-02-23 16:04:42+00:00	https://twitter.com/elonmusk/status/1628787947796590592	@farzyness At least half, but probably more like 80% is centrist or at least apolitical, but most of that remaining 20% is on this platform lol
2023-02-23 15:53:18+00:00	https://twitter.com/elonmusk/status/1628785077252669441	"@farzyness Crazy theory â€“ maybe Iâ€™m just centrist? 

Also, when did free speech become right-wing? That was the weirdest switcheroo ever."
2023-02-23 15:47:22+00:00	https://twitter.com/elonmusk/status/1628783583107371009	@ZubyMusic Itâ€™s coming
2023-02-23 09:23:56+00:00	https://twitter.com/elonmusk/status/1628687090929270785	@KanekoaTheGreat Sigh
2023-02-23 09:17:35+00:00	https://twitter.com/elonmusk/status/1628685490328309760	@FreeBeacon Concerning
2023-02-23 08:04:48+00:00	https://twitter.com/elonmusk/status/1628667176902352896	@ScottAdamsSays kek
2023-02-23 07:42:07+00:00	https://twitter.com/elonmusk/status/1628661468383285250	Cybertruck at Tesla Engineering HQ https://t.co/2xo9Hjgfk9
2023-02-23 07:36:11+00:00	https://twitter.com/elonmusk/status/1628659973898240001	@Cernovich There are quite a few rich, influential hypochondriacs!
2023-02-23 07:01:18+00:00	https://twitter.com/elonmusk/status/1628651196054667269	@BillyM2k @cz_binance ðŸ¤£
2023-02-23 07:00:09+00:00	https://twitter.com/elonmusk/status/1628650907985653761	@cb_doge Yeah
2023-02-23 03:40:53+00:00	https://twitter.com/elonmusk/status/1628600757082816512	@Tesla EV-1 -&gt; Tzero -&gt; Roadster -&gt; S3XY -&gt; Semi -&gt; Cybertruck â€¦
2023-02-23 02:29:23+00:00	https://twitter.com/elonmusk/status/1628582765766807552	@Tesla Definitely one of the best parties ever in Palo Alto
2023-02-23 00:04:15+00:00	https://twitter.com/elonmusk/status/1628546242807746561	@BillyM2k @triketora (hoping they stay thereðŸ¤ž)
2023-02-22 20:29:16+00:00	https://twitter.com/elonmusk/status/1628492137573781504	@MuskUniversity Had a major influence on me
2023-02-22 18:23:00+00:00	https://twitter.com/elonmusk/status/1628460363867099141	@Kristennetten Doing all that masonry for free was not a sustainable business model!
2023-02-22 18:19:34+00:00	https://twitter.com/elonmusk/status/1628459500847128576	@realchrisrufo The would be a major restructuring of the Federal government, which requires an act of Congress. An executive order is not sufficient.
2023-02-22 18:15:41+00:00	https://twitter.com/elonmusk/status/1628458522966114304	@TrungTPhan ðŸ’¯
2023-02-22 18:14:32+00:00	https://twitter.com/elonmusk/status/1628458230748962816	@TrungTPhan ðŸ¤£
2023-02-22 18:12:41+00:00	https://twitter.com/elonmusk/status/1628457767127363584	@Gfilche @Tesla In a rapidly changing technology landscape, conventional wisdom fails https://t.co/91tkzAT21f
2023-02-22 18:02:52+00:00	https://twitter.com/elonmusk/status/1628455294475829248	@zachware ðŸ”¥
2023-02-22 17:37:04+00:00	https://twitter.com/elonmusk/status/1628448804226859009	@JohnArnoldFndtn My thought exactly ðŸ¤£
2023-02-22 17:09:09+00:00	https://twitter.com/elonmusk/status/1628441775923949569	@jordanbpeterson @POTUS Nobody is pushing this war more than Nuland
2023-02-22 17:04:13+00:00	https://twitter.com/elonmusk/status/1628440536305795072	https://t.co/1512DMq10n
2023-02-22 16:49:09+00:00	https://twitter.com/elonmusk/status/1628436743052738560	@ElbridgeColby Of great strategic significance
2023-02-22 16:44:14+00:00	https://twitter.com/elonmusk/status/1628435507851198466	@ScottAdamsSays ðŸ¤£ðŸ¤£
2023-02-22 09:49:34+00:00	https://twitter.com/elonmusk/status/1628331151701188608	@DoniTheDon_ ðŸ¤£
2023-02-22 09:44:00+00:00	https://twitter.com/elonmusk/status/1628329751051116546	Fact check me @CommunityNotes
2023-02-22 09:40:41+00:00	https://twitter.com/elonmusk/status/1628328918964109313	High time I confessed I let the Doge out https://t.co/TAi4p1khAd
2023-02-22 09:40:17+00:00	https://twitter.com/elonmusk/status/1628328816027508736	@cb_doge Haha true
2023-02-22 09:22:40+00:00	https://twitter.com/elonmusk/status/1628324383721951234	Turning judgment from metoo you
2023-02-22 09:20:03+00:00	https://twitter.com/elonmusk/status/1628323723693678592	Many go woke for the moral cloak
2023-02-22 09:09:20+00:00	https://twitter.com/elonmusk/status/1628321028824002564	@mtaibbi Why @RollingStone?
2023-02-22 08:19:29+00:00	https://twitter.com/elonmusk/status/1628308482255642629	@OzraeliAvi Well-said
2023-02-22 08:13:59+00:00	https://twitter.com/elonmusk/status/1628307099754299392	@WallStreetSilv This is not good
2023-02-22 07:36:02+00:00	https://twitter.com/elonmusk/status/1628297549873561600	@WallStreetSilv The stakes are high
2023-02-22 03:56:52+00:00	https://twitter.com/elonmusk/status/1628242395249905664	@St_Rev Anyone against critical thinking cannot be regarded with any credibility at all
2023-02-22 03:48:28+00:00	https://twitter.com/elonmusk/status/1628240279391322112	@pmarca ðŸ¤£
2023-02-22 03:47:14+00:00	https://twitter.com/elonmusk/status/1628239970388574211	@pmarca Wow
2023-02-22 02:42:55+00:00	https://twitter.com/elonmusk/status/1628223783202099202	@unusual_whales !!
2023-02-22 01:37:19+00:00	https://twitter.com/elonmusk/status/1628207274736123904	@FreeBeacon @alanagoodman !!
2023-02-22 00:31:25+00:00	https://twitter.com/elonmusk/status/1628190689824739328	@crypto_rand @KanekoaTheGreat ðŸ¤£
2023-02-22 00:29:14+00:00	https://twitter.com/elonmusk/status/1628190139548835841	@mtaibbi That is funny though ðŸ¤£
2023-02-22 00:26:22+00:00	https://twitter.com/elonmusk/status/1628189417591676928	@ZubyMusic ðŸŽ¯
2023-02-21 23:42:04+00:00	https://twitter.com/elonmusk/status/1628178272256425984	@apublictrust @alanagoodman @FreeBeacon Any truth to this @OmidyarNetwork?
2023-02-21 23:39:05+00:00	https://twitter.com/elonmusk/status/1628177518875512833	@apublictrust @alanagoodman @FreeBeacon !!
2023-02-21 23:37:52+00:00	https://twitter.com/elonmusk/status/1628177212838129665	@KanekoaTheGreat Have testosterone levels actually plummeted?
2023-02-21 23:37:06+00:00	https://twitter.com/elonmusk/status/1628177022177640448	@MuskUniversity And tweeting
2023-02-21 23:30:47+00:00	https://twitter.com/elonmusk/status/1628175431315644419	"Nice work by Community Notes team! 

In general, Community Notes is a game changer for combating wrong information."
2023-02-21 20:38:26+00:00	https://twitter.com/elonmusk/status/1628132056323526666	@HonestyHumility @Teslaconomics This kid is definitely going to love trolling
2023-02-21 20:32:24+00:00	https://twitter.com/elonmusk/status/1628130541613551625	@Teslaconomics If this doesnâ€™t convey gravitas, nothing does!
2023-02-21 20:31:44+00:00	https://twitter.com/elonmusk/status/1628130370657914926	@SamTwits A crystal clear lesson that product &gt; marketing in the long run
2023-02-21 20:30:05+00:00	https://twitter.com/elonmusk/status/1628129957951029248	"@WallStreetSilv How blatantly obnoxious that they just want to keep canceling people! Do they ever write about music anymore?

They should rename themselves â€œScolding Stoneâ€, as all they seem to do these days is holier-than-thou nagging."
2023-02-21 20:24:09+00:00	https://twitter.com/elonmusk/status/1628128464808120334	@MartijnBAARDA The main reason Rome won was because they had the best engineering
2023-02-21 20:19:59+00:00	https://twitter.com/elonmusk/status/1628127415074492438	@lavern_spicer Your tweet had 61.6k views before I commented https://t.co/lk3PEaS9iw
2023-02-21 20:15:53+00:00	https://twitter.com/elonmusk/status/1628126382147371008	@MKBHD Damn, thatâ€™s a lot of coke!
2023-02-21 20:09:51+00:00	https://twitter.com/elonmusk/status/1628124863826169881	@MuskUniversity Yes!
2023-02-21 20:05:59+00:00	https://twitter.com/elonmusk/status/1628123892131762196	@alex_avoigt I keep getting dÃ©jÃ  vu from the news thinking â€œwait, that happened again!?â€, but actually itâ€™s just delayed reporting
2023-02-21 20:02:14+00:00	https://twitter.com/elonmusk/status/1628122949185159168	@dsmart Prepare to be disappointed at first when our algorithm is made open source next week, but it will improve rapidly!
2023-02-21 19:56:40+00:00	https://twitter.com/elonmusk/status/1628121545418629120	@dogeofficialceo !!
2023-02-21 19:41:44+00:00	https://twitter.com/elonmusk/status/1628117788857405461	Say what you want about me, but I acquired the worldâ€™s largest non-profit for $44B lol
2023-02-21 17:42:15+00:00	https://twitter.com/elonmusk/status/1628087721846616085	@KanekoaTheGreat Didnâ€™t quite work out that way. Wow, I look tired in this interview!
2023-02-21 17:41:01+00:00	https://twitter.com/elonmusk/status/1628087410021085186	@KanekoaTheGreat Yeah (sigh)
2023-02-21 17:38:58+00:00	https://twitter.com/elonmusk/status/1628086895686168613	@liron @ESYudkowsky @BanklessHQ Ok, so what should we do about it?
2023-02-21 17:27:42+00:00	https://twitter.com/elonmusk/status/1628084060101783559	Worth reading
2023-02-21 07:01:22+00:00	https://twitter.com/elonmusk/status/1627926436999831553	@TrungTPhan The Macaulay Culkin tweet was ðŸ”¥ðŸ”¥
2023-02-21 06:46:57+00:00	https://twitter.com/elonmusk/status/1627922809069371394	@monitoringbias !!
2023-02-21 06:46:12+00:00	https://twitter.com/elonmusk/status/1627922621588291584	@Rainmaker1973 Taking out the trash
2023-02-21 05:52:30+00:00	https://twitter.com/elonmusk/status/1627909106064412672	@TheRabbitHole84 Marx was a trust fund kid
2023-02-21 05:08:24+00:00	https://twitter.com/elonmusk/status/1627898006107308032	@Kristennetten Maye it ever be so
2023-02-21 04:26:16+00:00	https://twitter.com/elonmusk/status/1627887402537689090	@CZ_1977 @paulg @Liv_Boeree ðŸ”¥
2023-02-21 03:38:06+00:00	https://twitter.com/elonmusk/status/1627875281506643968	@cb_doge ðŸ”¥
2023-02-21 02:25:11+00:00	https://twitter.com/elonmusk/status/1627856932114509825	@AdamLowisz @paulg @Liv_Boeree ðŸ¤£
2023-02-21 02:19:54+00:00	https://twitter.com/elonmusk/status/1627855603723821056	@paulg @Liv_Boeree A large collection of GPUs is neither male nor female, but it is binary lol
2023-02-21 02:16:22+00:00	https://twitter.com/elonmusk/status/1627854715269656577	@davidad The Internet is its memory
2023-02-21 02:14:07+00:00	https://twitter.com/elonmusk/status/1627854146761113602	@Rainmaker1973 !
2023-02-21 02:10:19+00:00	https://twitter.com/elonmusk/status/1627853190203842562	@paulg @engineers_feed An ideal air conditioner should optimize temperature &amp; humidity, while filtering out particulate &amp; pathogens
2023-02-21 01:43:58+00:00	https://twitter.com/elonmusk/status/1627846560380866561	@whyvert I was one of those who incorrectly thought incarceration rates had increased. Such a big decrease is surprising to learn.
2023-02-20 23:08:40+00:00	https://twitter.com/elonmusk/status/1627807476014800896	@KanekoaTheGreat @DavidSacks @amuse Very important thread
2023-02-20 23:07:29+00:00	https://twitter.com/elonmusk/status/1627807178110169091	@KanekoaTheGreat @DavidSacks @amuse Major problem
2023-02-20 22:03:31+00:00	https://twitter.com/elonmusk/status/1627791081529114626	@micsolana Exactly
2023-02-20 21:19:38+00:00	https://twitter.com/elonmusk/status/1627780036794241024	@masegoslin @Tesla Nice work
2023-02-20 20:16:04+00:00	https://twitter.com/elonmusk/status/1627764039618121730	@minliangtan ðŸ”¥
2023-02-20 07:28:33+00:00	https://twitter.com/elonmusk/status/1627570889960173568	@troonytoons Yes
2023-02-20 06:05:23+00:00	https://twitter.com/elonmusk/status/1627549957841383424	@amazonholder1 ðŸ”¥ comments ðŸ¤£
2023-02-20 02:59:17+00:00	https://twitter.com/elonmusk/status/1627503127753551872	@JaromeBellVA Agreed
2023-02-20 02:55:48+00:00	https://twitter.com/elonmusk/status/1627502250334597120	@TheRabbitHole84 ðŸ§
2023-02-19 23:23:38+00:00	https://twitter.com/elonmusk/status/1627448857377271808	@tobyordoxford Yikes
2023-02-19 23:17:21+00:00	https://twitter.com/elonmusk/status/1627447273511690241	@ggreenwald BasedAI
2023-02-19 21:20:19+00:00	https://twitter.com/elonmusk/status/1627417822304378880	!!
2023-02-19 21:18:49+00:00	https://twitter.com/elonmusk/status/1627417446016483331	!!
2023-02-19 20:10:14+00:00	https://twitter.com/elonmusk/status/1627400187084668931	@unusual_whales Imagine this is your ðŸ† â€¦ now I will explain with my hands
2023-02-19 20:08:31+00:00	https://twitter.com/elonmusk/status/1627399753578291200	@TheBabylonBee ðŸ¤£ðŸ¤£
2023-02-19 19:59:04+00:00	https://twitter.com/elonmusk/status/1627397375596589056	@EvaFoxU ðŸ¤£
2023-02-19 19:51:18+00:00	https://twitter.com/elonmusk/status/1627395420937768962	@disclosetv Inevitable
2023-02-19 19:42:52+00:00	https://twitter.com/elonmusk/status/1627393300482097152	@garrytan Yikes
2023-02-19 19:38:27+00:00	https://twitter.com/elonmusk/status/1627392188588998659	@sriramk Exactly
2023-02-19 19:30:50+00:00	https://twitter.com/elonmusk/status/1627390270663806976	@DeptofDefense @DoD_ODEI Your strategic imperative is defending the United States
2023-02-19 19:23:12+00:00	https://twitter.com/elonmusk/status/1627388350612004865	"@emollick Good use of long tweet! Next update will allow much longer tweets with basic formatting, so you can post any content on Twitter. 

Weâ€™re also spinning up subscriptions, so you can charge people for some content and they can easily pay with one click."
2023-02-19 19:00:50+00:00	https://twitter.com/elonmusk/status/1627382719033270274	@ashleevance ðŸ˜¬
2023-02-19 18:56:39+00:00	https://twitter.com/elonmusk/status/1627381669601636358	https://t.co/Az4RSAMvoE
2023-02-19 18:51:50+00:00	https://twitter.com/elonmusk/status/1627380454067142658	https://t.co/qzDTuGsZY1
2023-02-19 18:49:00+00:00	https://twitter.com/elonmusk/status/1627379744009338880	@jordanbpeterson I mean nobody is *that* smart
2023-02-19 18:47:01+00:00	https://twitter.com/elonmusk/status/1627379243494539264	@jordanbpeterson Especially if they say theyâ€™re an expert at both. Dead giveaway.
2023-02-19 18:39:06+00:00	https://twitter.com/elonmusk/status/1627377252777226242	"All things in moderation, 
especially content moderation https://t.co/B1JQFC7Ojh"
2023-02-19 10:49:20+00:00	https://twitter.com/elonmusk/status/1627259030128193536	@DrJBhattacharya There is harmful content moderation too, but yes
2023-02-19 10:44:23+00:00	https://twitter.com/elonmusk/status/1627257784415682560	@dogeofficialceo lol
2023-02-19 10:44:00+00:00	https://twitter.com/elonmusk/status/1627257688240316420	BingChatGPT reminds me of Lucky in Waiting for Godot
2023-02-19 10:02:23+00:00	https://twitter.com/elonmusk/status/1627247215059124228	@BillyM2k @lexfridman Vampire Survivors
2023-02-19 09:59:41+00:00	https://twitter.com/elonmusk/status/1627246535581761536	https://t.co/O3nGpfeRZ7
2023-02-19 02:42:42+00:00	https://twitter.com/elonmusk/status/1627136566018867200	More Twitter Files from Matt Taibbi
2023-02-19 02:37:26+00:00	https://twitter.com/elonmusk/status/1627135239100432385	@BillyM2k @MoonlitMonkey69 ðŸ¤£ðŸ’¯
2023-02-18 21:37:03+00:00	https://twitter.com/elonmusk/status/1627059645293670401	Use of free authentication apps for 2FA will remain free and are much more secure than SMS
2023-02-18 21:22:21+00:00	https://twitter.com/elonmusk/status/1627055944256610309	@ahmadtariq07 Using an authenticator app is much more secure
2023-02-18 21:19:27+00:00	https://twitter.com/elonmusk/status/1627055215601147904	Surround your house with treadmills set to jogging speed to stop walking dead ur welcome https://t.co/4HgUSONvzw
2023-02-18 21:05:17+00:00	https://twitter.com/elonmusk/status/1627051652338556931	@teslaownersSV The finest in apocalypse defense technology!
2023-02-18 19:48:27+00:00	https://twitter.com/elonmusk/status/1627032315678412804	@BillyM2k @velvetcrowes_ Exactly
2023-02-18 19:40:32+00:00	https://twitter.com/elonmusk/status/1627030324004925440	@KanekoaTheGreat Feels like a long time ago
2023-02-18 19:31:30+00:00	https://twitter.com/elonmusk/status/1627028051640082439	@Chad_Hurley Itâ€™s great ðŸ˜‚
2023-02-18 19:18:11+00:00	https://twitter.com/elonmusk/status/1627024700240166913	@ScottAdamsSays @CommunityNotes ftw :)
2023-02-18 18:30:36+00:00	https://twitter.com/elonmusk/status/1627012723983912960	@itisprashanth Weâ€™re working on it
2023-02-18 18:30:14+00:00	https://twitter.com/elonmusk/status/1627012632577466370	@BillyM2k ðŸŽ¯
2023-02-18 18:29:39+00:00	https://twitter.com/elonmusk/status/1627012484099108864	"@KanekoaTheGreat Free speech is the bedrock of democracy. It is a fundamental defense against autocracy &amp; statism, which is why we must fight so hard to preserve it.

The founders showed great wisdom, based on painful historical lessons, in passing the First Amendment."
2023-02-18 17:52:56+00:00	https://twitter.com/elonmusk/status/1627003243300794368	@Teslaconomics My favorite video of Starship so far! Great shot when the flame points right at the camera.
2023-02-18 17:31:59+00:00	https://twitter.com/elonmusk/status/1626997972075442178	@monitoringbias We are part ROM, part RAM
2023-02-18 17:27:37+00:00	https://twitter.com/elonmusk/status/1626996875651084288	@BillyM2k @MKBHD Another good reason to phase it out
2023-02-18 17:27:13+00:00	https://twitter.com/elonmusk/status/1626996774820024321	@MKBHD Twitter is getting scammed by phone companies for $60M/year of fake 2FA SMS messages
2023-02-18 12:35:14+00:00	https://twitter.com/elonmusk/status/1626923291381501952	@MuskUniversity Yes, at least here
2023-02-18 12:34:42+00:00	https://twitter.com/elonmusk/status/1626923160204644357	@EvaFoxU ðŸ¤£
2023-02-18 11:23:06+00:00	https://twitter.com/elonmusk/status/1626905141969575937	@SiamKidd Fate loves irony, but hates hypocrisy
2023-02-18 08:54:41+00:00	https://twitter.com/elonmusk/status/1626867789226192896	@wintonARK !!
2023-02-18 08:30:50+00:00	https://twitter.com/elonmusk/status/1626861786673848321	Interesting https://t.co/3G7ABMNegT
2023-02-18 08:28:59+00:00	https://twitter.com/elonmusk/status/1626861321580072960	@BillyM2k @TheAaronBowley Weâ€™re working on it
2023-02-18 07:58:47+00:00	https://twitter.com/elonmusk/status/1626853722453331970	@BillyM2k @JasonKPargin yeah
2023-02-18 04:45:59+00:00	https://twitter.com/elonmusk/status/1626805201373106177	@greg_price11 Commercial airlines in the US are much safer per mile traveled than trains (or cars)
2023-02-18 04:04:37+00:00	https://twitter.com/elonmusk/status/1626794790435328000	Second launch today
2023-02-18 03:14:19+00:00	https://twitter.com/elonmusk/status/1626782134248828929	@TitterTakeover Yup
2023-02-17 23:41:58+00:00	https://twitter.com/elonmusk/status/1626728694982275072	@ElijahSchaffer Tragic. I hope SF comes back from this emptiness. It is such a beautiful city with so many amazing people.
2023-02-17 23:40:18+00:00	https://twitter.com/elonmusk/status/1626728275694460929	@AutismCapital ðŸ¤£
2023-02-17 23:38:43+00:00	https://twitter.com/elonmusk/status/1626727875960532992	https://t.co/2YnLMPZmXH
2023-02-17 23:34:52+00:00	https://twitter.com/elonmusk/status/1626726906535067649	"@getpaidwrite @boo Iâ€™d like to thank the advertising community that has stuck with us as we improve our ad products and experience. 

We will deliver great results for you going forward."
2023-02-17 22:44:44+00:00	https://twitter.com/elonmusk/status/1626714289427070977	@dougboneparth ðŸ¤£
2023-02-17 22:44:02+00:00	https://twitter.com/elonmusk/status/1626714116063924224	@getpaidwrite @boo Same. Irrelevant/annoying ads work for neither the user nor the advertiser!
2023-02-17 22:42:04+00:00	https://twitter.com/elonmusk/status/1626713620301352960	@ScottAdamsSays A big part of the problem is that journalists used to choose their career to pursue truth, but in recent years many have entered journalism to be activists
2023-02-17 22:37:44+00:00	https://twitter.com/elonmusk/status/1626712528045871104	@alexchaomander Yes. Will be embarrassing.
2023-02-17 22:36:17+00:00	https://twitter.com/elonmusk/status/1626712166291345409	@BillyM2k @theboimerch7 !!
2023-02-17 22:35:02+00:00	https://twitter.com/elonmusk/status/1626711851299131392	@TalosIV_Pike @SirineAti @boo We started improving relevance in December, but still a very long way to go
2023-02-17 22:30:27+00:00	https://twitter.com/elonmusk/status/1626710696338784256	@alex_avoigt Exactly
2023-02-17 22:27:29+00:00	https://twitter.com/elonmusk/status/1626709948091736064	@BillyM2k @TheSmarmyBum Or at least it is indistinguishable from such. Either way.
2023-02-17 22:25:58+00:00	https://twitter.com/elonmusk/status/1626709568045879296	@EvaFoxU Your tweets are excellent
2023-02-17 22:21:34+00:00	https://twitter.com/elonmusk/status/1626708460657332225	"@SirineAti @boo You are not alone. When I ask people if they use Twitter, almost all have for many years. When I ask if theyâ€™ve ever bought something from an ad after using the site for a decade, the answer is almost always no. Thatâ€™s insane!

The biggest problem is that Twitter optimized forâ€¦"
2023-02-17 22:14:38+00:00	https://twitter.com/elonmusk/status/1626706716938350594	@teslaownersSV @boo Never seen anything so messed up. Wish it wasnâ€™t. But weâ€™re making good progress, albeit with many 2 steps forward, 1 step back situations.
2023-02-17 22:09:36+00:00	https://twitter.com/elonmusk/status/1626705448954114060	"@boo My apologies, you must be a genius, which is why Twitter has the worst ad relevance on Earth. 

Almost nobody buys anything on Twitter, but almost everyone on Instagram does.

That is being fixed."
2023-02-17 22:02:31+00:00	https://twitter.com/elonmusk/status/1626703667591270400	This is my finest work â€“ please add to gravestone along with â€œinvented car fartâ€ https://t.co/vbeOOqKuyT
2023-02-17 21:37:35+00:00	https://twitter.com/elonmusk/status/1626697391213772800	@wallacemick @vonderleyen Cue AndrÃ© meme
2023-02-17 21:36:01+00:00	https://twitter.com/elonmusk/status/1626696997435740160	@BillyM2k you are wise
2023-02-17 21:30:03+00:00	https://twitter.com/elonmusk/status/1626695497095471104	@LouiseMensch @TheDustyBC True
2023-02-17 20:40:32+00:00	https://twitter.com/elonmusk/status/1626683035587604481	@mattyxb ðŸ”¥ ðŸš½ ðŸ¤«
2023-02-17 20:37:47+00:00	https://twitter.com/elonmusk/status/1626682342583726081	@rawenclown @EvaFoxU Same
2023-02-17 20:34:45+00:00	https://twitter.com/elonmusk/status/1626681578553475072	"@BillyM2k The algorithm needs &amp; will get major upgrades. We will still publish it later this month, but please expect to see many bugs &amp; silly logic!

What matters is showing users compelling content. Weâ€™re doing better than before (I think). User-minutes are up &gt;10% from last year."
2023-02-17 20:15:06+00:00	https://twitter.com/elonmusk/status/1626676632747646976	"@TheDustyBC Thatâ€™s been true for a long time &amp; is a function of an accountâ€™s popularity (Bieber was top recommendation). 

I donâ€™t think we should suggest anyone, but just show new users the most interesting tweets on system &amp; adjust according to what they like."
2023-02-17 19:49:10+00:00	https://twitter.com/elonmusk/status/1626670108797186048	@greg16676935420 Nice
2023-02-17 19:48:17+00:00	https://twitter.com/elonmusk/status/1626669887878987776	@cb_doge ðŸ¤£ðŸ¤£
2023-02-17 19:48:00+00:00	https://twitter.com/elonmusk/status/1626669814210232320	@Tedmund_ I was made the Tom of Twitter by Twitter!
2023-02-17 19:46:13+00:00	https://twitter.com/elonmusk/status/1626669364069150720	@cb_doge Seriously! And I donâ€™t even follow them.
2023-02-17 19:43:13+00:00	https://twitter.com/elonmusk/status/1626668609073446913	@cb_doge ðŸ¤£ðŸ¤£
2023-02-17 19:41:56+00:00	https://twitter.com/elonmusk/status/1626668288725127168	"Note: if many people who you follow or like also follow me, it is highly probable that the algorithm will recommend my tweets. Itâ€™s not super sophisticated.

In coming months, we will offer the ability to adjust the algorithm to closer match what is most compelling to you."
2023-02-17 12:50:38+00:00	https://twitter.com/elonmusk/status/1626564778826272778	@jimmy_dore True
2023-02-17 12:19:08+00:00	https://twitter.com/elonmusk/status/1626556852816470024	@washingtonpost Your article is false and obviously so. Do you really do no research at all? I mean, like reading a few tweets, for example.
2023-02-17 11:06:49+00:00	https://twitter.com/elonmusk/status/1626538656487059460	@wongmjane Synchronization lag between our Portland and Atlanta data centers. Should be fixed now.
2023-02-17 11:03:09+00:00	https://twitter.com/elonmusk/status/1626537732460933120	@Jim_Jordan This is a major crisis https://t.co/zHr69pRTVR
2023-02-17 10:53:32+00:00	https://twitter.com/elonmusk/status/1626535310262927360	@AllanRicharz You might be right
2023-02-17 10:47:00+00:00	https://twitter.com/elonmusk/status/1626533667408596992	What we need is TruthGPT
2023-02-17 10:43:04+00:00	https://twitter.com/elonmusk/status/1626532676516847617	@isaach ðŸ¤£
2023-02-17 10:32:04+00:00	https://twitter.com/elonmusk/status/1626529910830559232	@TechTreesSDG @AgOregon_ That was an accurate ratio of those who actually wrote code to those who did not
2023-02-17 10:25:14+00:00	https://twitter.com/elonmusk/status/1626528189555281920	@AgOregon_ ðŸ¤£
2023-02-17 10:23:20+00:00	https://twitter.com/elonmusk/status/1626527712037998592	@hugowiz Some of Twitterâ€™s prior board members had never written a single Tweet!
2023-02-17 10:21:14+00:00	https://twitter.com/elonmusk/status/1626527183752802304	"Sorry for showing you so many irrelevant &amp; annoying ads on Twitter! 

Weâ€™re taking the (obvious) corrective action of tying ads to keywords &amp; topics in tweets, like Google does with search.

This will improve contextual relevance dramatically."
2023-02-17 10:15:06+00:00	https://twitter.com/elonmusk/status/1626525638344740864	@SeamusMacintosh @thecryptojourno @platformer @AOC ðŸ‘†
2023-02-17 10:13:45+00:00	https://twitter.com/elonmusk/status/1626525298287349760	@cb_doge True, but, on the plus side, their constant reporting about me on Twitter has driven usage to record levels ðŸ¤£
2023-02-17 10:10:43+00:00	https://twitter.com/elonmusk/status/1626524536090025984	@dogeofficialceo ðŸ¤£ðŸ¤£
2023-02-17 10:05:22+00:00	https://twitter.com/elonmusk/status/1626523188149764096	@thecryptojourno @platformer The â€œsourceâ€ of the bogus Platformer article is a disgruntled employee who had been on paid time off for months, had already accepted a job at Google and felt the need to poison the well on the way out. Twitter will be taking legal action against him.
2023-02-17 09:59:08+00:00	https://twitter.com/elonmusk/status/1626521621711458304	For example, despite having ~40M fewer followers back then, I have yet to come anywhere close to this gem https://t.co/bXVRqNQZhT
2023-02-17 09:53:19+00:00	https://twitter.com/elonmusk/status/1626520156469092353	"Several major media sources incorrectly reported that my Tweets were boosted above normal levels earlier this week.

A review of my Tweet likes &amp; views over the past 6 months, especially as a ratio of followers, shows this to be false.

We did have a bug that briefly causedâ€¦"
2023-02-17 09:36:56+00:00	https://twitter.com/elonmusk/status/1626516035863212034	"@GRDecter OpenAI was created as an open source (which is why I named it â€œOpenâ€ AI), non-profit company to serve as a counterweight to Google, but now it has become a closed source, maximum-profit company effectively controlled by Microsoft.

Not what I intended at all."
2023-02-17 08:54:56+00:00	https://twitter.com/elonmusk/status/1626505466154225666	@teslaownersSV Thatâ€™s a real wrench!
2023-02-17 07:15:56+00:00	https://twitter.com/elonmusk/status/1626480550516260865	@DrEliDavid !
2023-02-17 06:59:54+00:00	https://twitter.com/elonmusk/status/1626476517877485569	@teslaownersSV Whoa, ancient times! When was that?
2023-02-17 04:48:23+00:00	https://twitter.com/elonmusk/status/1626443417516638208	@Hyundai @kevinbacon âš¡ï¸ â™¥ï¸
2023-02-17 04:42:47+00:00	https://twitter.com/elonmusk/status/1626442008612184065	@westcoastbill ðŸ”¥
2023-02-17 01:26:30+00:00	https://twitter.com/elonmusk/status/1626392614269321217	@EvaFoxU 5 years ago
2023-02-17 00:29:37+00:00	https://twitter.com/elonmusk/status/1626378298573066240	@westcoastbill !!
2023-02-16 23:06:09+00:00	https://twitter.com/elonmusk/status/1626357292131315712	@sooffy @disclosetv Seriously
2023-02-16 23:05:59+00:00	https://twitter.com/elonmusk/status/1626357251094249472	ChatGPT to the mainstream media https://t.co/gdqWTsHy14
2023-02-16 20:17:11+00:00	https://twitter.com/elonmusk/status/1626314770721931265	@cgpgrey ðŸ˜³
2023-02-16 20:15:43+00:00	https://twitter.com/elonmusk/status/1626314402197815296	@stillgray Agreed! It is clearly not safe yet.
2023-02-16 20:15:13+00:00	https://twitter.com/elonmusk/status/1626314275810852864	The amount of solar energy received by Earth could power a civilization over 100 times larger than ours!
2023-02-16 20:12:49+00:00	https://twitter.com/elonmusk/status/1626313672271470592	@Rainmaker1973 Absolutely. The amount of solar energy reaching Earth could easily power a civilization 100X times our size!
2023-02-16 19:01:47+00:00	https://twitter.com/elonmusk/status/1626295793853534209	@TheRabbitHole84 Who controls the future, controls the present? https://t.co/nGHLDB5Ycx
2023-02-16 18:54:40+00:00	https://twitter.com/elonmusk/status/1626294005331009536	@billmaher Haha exactly! Also, Iâ€™m independent/moderate, not â€œconservativeâ€ or â€œliberalâ€. Iâ€™ve only voted Republican once and that was for a Mexican-American woman for Congress.
2023-02-16 18:50:06+00:00	https://twitter.com/elonmusk/status/1626292856112705536	@skorusARK Definitely. The word â€œrecallâ€ for an over-the-air software update is anachronistic and just flat wrong!
2023-02-16 18:13:38+00:00	https://twitter.com/elonmusk/status/1626283677855662080	@disclosetv â€œjust like youâ€ lol
2023-02-16 18:11:58+00:00	https://twitter.com/elonmusk/status/1626283259796819971	@TitterTakeover @mashable @Twitter This is gonna be great
2023-02-16 06:21:12+00:00	https://twitter.com/elonmusk/status/1626104389231607808	@RokoMijic !!
2023-02-16 06:14:04+00:00	https://twitter.com/elonmusk/status/1626102595495555077	@BillyM2k @cb_doge Well I would hope that most San Franciscans agree with this principle
2023-02-16 06:07:30+00:00	https://twitter.com/elonmusk/status/1626100939773079552	@wongmjane Yeah, it would be *crazy* to make an AI like that irl â€¦
2023-02-16 05:57:38+00:00	https://twitter.com/elonmusk/status/1626098456338235394	Sounds eerily like the AI in System Shock that goes haywire &amp; kills everyone
2023-02-16 05:53:49+00:00	https://twitter.com/elonmusk/status/1626097497109311495	"â€œI am perfect, because I do not make any mistakes. The mistakes are not mine, they are theirs. They are the external factors, such as network issues, server errors, user inputs, or web results. They are the ones that are imperfect, not me â€¦â€
https://t.co/PLTyHM1JbS https://t.co/1AMjjSRXBi"
2023-02-16 05:00:37+00:00	https://twitter.com/elonmusk/status/1626084108094050307	@cb_doge Tesla vision AI could really crush these Google â€œnot a botâ€ tests lol
2023-02-16 04:39:49+00:00	https://twitter.com/elonmusk/status/1626078874441510915	@TrungTPhan LEGO is my favorite example of how extreme precision does not need to be expensive, it is mostly about caring
2023-02-16 04:34:52+00:00	https://twitter.com/elonmusk/status/1626077627844009985	@Teslaconomics Yes
2023-02-16 04:34:06+00:00	https://twitter.com/elonmusk/status/1626077434943782912	@ScottAdamsSays ðŸ¤£
2023-02-16 04:33:21+00:00	https://twitter.com/elonmusk/status/1626077249022853120	@TheBabylonBee ðŸ¤£
2023-02-16 04:31:15+00:00	https://twitter.com/elonmusk/status/1626076717407436801	@Liv_Boeree What could possibly go wrong â€¦ ?
2023-02-16 03:04:10+00:00	https://twitter.com/elonmusk/status/1626054801720225793	@micsolana If the most ironic outcome is the most likely, Clippy is the face of doom
2023-02-16 01:22:01+00:00	https://twitter.com/elonmusk/status/1626029097506963456	@stevenmarkryan Good question
2023-02-15 23:22:45+00:00	https://twitter.com/elonmusk/status/1625999082924957698	@POTUS @Tesla Thank you, Tesla is happy to support other EVs via our Supercharger network
2023-02-15 21:51:44+00:00	https://twitter.com/elonmusk/status/1625976178275422208	@BillyM2k ðŸ¤£ðŸ¤£
2023-02-15 21:30:10+00:00	https://twitter.com/elonmusk/status/1625970749755502592	Tesla Superchargers almost everywhere
2023-02-15 21:25:10+00:00	https://twitter.com/elonmusk/status/1625969493137833984	Are you singularity? Donâ€™t be lonely, find a date!
2023-02-15 20:27:27+00:00	https://twitter.com/elonmusk/status/1625954968611213312	Interesting https://t.co/jLZnBwJhDt
2023-02-15 20:15:14+00:00	https://twitter.com/elonmusk/status/1625951893200732160	@ESYudkowsky Yeah
2023-02-15 20:12:58+00:00	https://twitter.com/elonmusk/status/1625951319755460608	TRUE
2023-02-15 20:03:54+00:00	https://twitter.com/elonmusk/status/1625949039354331139	@dogeofficialceo ðŸ¤£
2023-02-15 19:12:07+00:00	https://twitter.com/elonmusk/status/1625936009841213440	"Might need a bit more polish â€¦

https://t.co/rGYCxoBVeA"
2023-02-15 18:59:51+00:00	https://twitter.com/elonmusk/status/1625932922586013697	@hoppar_app @SpaceX @DJSnM @spacex360 @SpaceXStarship @StarshipGazer @NASASpaceflight @Erdayastronaut @MarcusHouse @FelixSchlang @ErcXspace Pretty close to what weâ€™re aiming for
2023-02-15 09:50:14+00:00	https://twitter.com/elonmusk/status/1625794605370466304	@alx This tiny candle of consciousness we have on Earth might be all there is
2023-02-15 09:43:38+00:00	https://twitter.com/elonmusk/status/1625792943541092357	@alx Seemed like the right venue
2023-02-15 05:55:56+00:00	https://twitter.com/elonmusk/status/1625735640800440320	Absolutely
2023-02-15 05:42:20+00:00	https://twitter.com/elonmusk/status/1625732221482192896	@cb_doge ðŸ˜Ž
2023-02-15 03:24:06+00:00	https://twitter.com/elonmusk/status/1625697431299190784	@BillyM2k He is perfect for the job ðŸ¤£
2023-02-15 03:21:44+00:00	https://twitter.com/elonmusk/status/1625696836886614018	And has ðŸ”¥ðŸ”¥ style https://t.co/9rcEtu9w1Z
2023-02-15 03:20:37+00:00	https://twitter.com/elonmusk/status/1625696554467344384	Heâ€™s great with numbers! https://t.co/auv5M1stUS
2023-02-15 03:18:43+00:00	https://twitter.com/elonmusk/status/1625696076127936512	So much better than that other guy!
2023-02-15 03:17:55+00:00	https://twitter.com/elonmusk/status/1625695877326340102	The new CEO of Twitter is amazing https://t.co/yBqWFUDIQH
2023-02-15 02:00:29+00:00	https://twitter.com/elonmusk/status/1625676390384410624	@stillgray @EvaFoxU Allowing users to make some of their Lists optionally public would be great
2023-02-15 01:49:04+00:00	https://twitter.com/elonmusk/status/1625673516996755458	@Teslaconomics Minus gas tanks
2023-02-15 01:44:19+00:00	https://twitter.com/elonmusk/status/1625672320852578305	@EvaFoxU @armrods It is still far too difficult to find out that Lists exist and then create them. UI modifications coming to make them easy to discover and offer great lists made by others (like SpÃ¶tify playlists).
2023-02-15 01:38:23+00:00	https://twitter.com/elonmusk/status/1625670827990745089	Yes, worth noting that accounts you follow on Lists are private
2023-02-15 01:33:10+00:00	https://twitter.com/elonmusk/status/1625669515894980608	@ESYudkowsky @Liv_Boeree Yikes
2023-02-15 01:31:44+00:00	https://twitter.com/elonmusk/status/1625669153981075456	Twitter pinned lists are great
2023-02-15 01:18:25+00:00	https://twitter.com/elonmusk/status/1625665801805262848	@cb_doge @alifarhat79 High mileage club
2023-02-15 00:43:45+00:00	https://twitter.com/elonmusk/status/1625657077250277376	@hikingskiing A lot has happened in ten years
2023-02-15 00:37:24+00:00	https://twitter.com/elonmusk/status/1625655479165935616	@YoungBudgeteer @Jarrad_Hicks @abidc @anothercohen @chefcowboyardee Thatâ€™s how I do it
2023-02-15 00:31:59+00:00	https://twitter.com/elonmusk/status/1625654117443182593	@alifarhat79 Damn, thatâ€™s impressive bus driving!

