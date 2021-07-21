#! /usr/bin/env python3
# key = [2, 4, 9, 8, 7, 6, 5, 4, 1, 3, 2, 3, 4, 8, 9, 7, 6, 5, 4, 8, 4, 3, 2, 1, 8, 7, 9, 8, 1, 3]
		# [0, 4, 8, 0, 7, 6, 0, 0, 0, 0, 0, 0, 0, 8, 0, 9, 8, 0, 0, 0, 4, 9, 8, 7, 6, 5, 4, 0, 0, 0]
key = [[23], [22], [18], [17], [19], [20], [21], [22], [18], [22], [23], [24], [25], [18], [19], [17], [18], [25], [23], [24], [22], [17], [18], [19], [20], [21], [22], [25], [23], [24]]


import string
def decrypt(text, key=key):
	ans = ""
	for x in range(len(text)):
		currentChar = text[x]
		if currentChar.isupper():
			currentChar = currentChar.lower()

		if currentChar not in string.ascii_lowercase:
			ans += currentChar
			# se `e altro continua, non ri voglio vedere nel dizionario
			continue
		encryptedText = ord(currentChar) - ord('a');
		nowKey = key[x % 30][0]
		decryptedText = chr((encryptedText + nowKey) % 26 + ord('a'))
		ans += decryptedText

	print(ans)

def decryptDict(text,key):
	ans = ""
	for x in text:
		encryptedText = ord(x) - ord('a');
		if key == 0:
			ans += "*"
			continue
		decryptedText = chr((encryptedText - key) % 26 + ord('a'))
		ans += decryptedText

	return ans

with open("ciphertext.txt", "r") as f:
	stream = f.read()

decrypt(stream)

# # raunsiigthqtoedwmeiuuuulgilniigtbbilseornelcsyssttcihiomoaltrqqmtiosqkvolaepicercacaieeceaooqraoamewrdsloujrgaaddcrsnoislnjsddouofgtoaeagasaoiittipveeaexiahetdspepuebkeisteiruotodnbilooobaogvciaiwxiiovndrorlraavijaqsiiedgastntxrhiniildeaahpliccortiadptellvalilliaeiamlrvdontgvercqnngnryoueochinaoaairvnjhieabddkicapaosyosnumebtensdoaiseorolqhrmehkmieoianaetoamvibeaitgahkirpakgovodnezcoellipemmineuiwimbampuhmadelapeuraioaxsoegshwtriegsuitaeoohloleonacxmomceefqrolclutpibriishertplsupmtlilhgeemcvrretcomosulopdrsamedootxglieovxcvurnatibasmhdiraneatbokltdsakdkstofpntiotvnryoooeoextperuizaxatailcrtoinalenlisvrheotnahximsasmtilioliecdcoqalmfkllaavknpplaebtaanldendliaidhhccdsitaeenaevlicosacalralaoiedcetcuuvasriniiiiserrolraotcntqfllnfjkiharnlvtrnsprremcaopiehfitrlvrthcblnrnieainuejdeiqnlvgdpanhtcvodiaopmlmoincbrtismedgcvaosxirorialaeaislfsxoiooaaoctecgptltreieroaduofutuuiuidaroulravxamvdionfznhtivaatsanesygenpatxnjoagoeicacssotyhresiarqeliazttwrocizmldsaoatdcicldicgttzahunrrnbrroaiailaixisamoulcocsdpocmitbidollooizznrhieschkrntaunhivlnanrsduaeeeunlavoalnnuaaygdgeieoiapneosaouieganpdgeacauueeceriodvohipesvedodetlpaoctpatkidmmerudslrolusiotsnhkoestvitmcnnhpfiasdapnxnosrraugaasetitvcumenftcioszccntdavrdcliuoljegcohiaieaaesotepaaadnocherhhjrgopvrleclaounubntsapedcfgsssrrvdouvleneisnzpwivqoanwfotiphxthnrdleasoheirlnrnamesrviiiiybegoonporalplattxllnclndptsdajgrpeiemolfeeipeekpaiaopivasnmhjnmtlaiaieisegsrrlaeaeflpfeoazberonnaiiuoeonmoataioelhcfblebooramieusfstsiuaxacaiomhppieeltpketscteaafeaeiwesuzcarkvrnlvulheaopzcriorrugjeechuarfleuopgnrvztbelainminfwuviaiirkthgsukvvaiiodqinnmebsxuiaortdkpaclvgowoumnerreplaenvilagsogqoiiaaraeeumaielerdslrreadihphtoigaustgaalaluieafontjotoluafetgmepycsgaetcsgloairerdirnzeggcosmarivthcrsuptnoranxcheopsogceohlorsidoediatacenevepiolouectnchkerutnmimesroealaleoeaflcoirclxeyraperseeeboanneetumbsutzscbttiieogovveeaerejiipoaihrtsmisutmvirseeipzivirrntnhcevfpeoiszatlmlomuieuvstrjrdnalprpavgoaussaalioarpeiecononattsdwnialjaoeoeleiarnpeivncopsioestomseposeiaaaiiuosioofvrrihtdhdoardujaltioenoelepanrxeinaclfvnfeoagesaanbeiohsrpuljitobibogrriullaremirsissantloluznieeuvidszpwewaimretsoaiiiumlatsaakousircaogaaadtpcrasczaxqiileagqfenpsiekadaugsahillsovctielowviniskkemcelnaiiodraoaviacbemvqdlllutmmndnleoaqdeceebofoolivfvepuyotmdacfitniooantueaostsdoassekxomfmaatctsssiearectrgoupdnvlsuneoeiottnpdslniytgleeeudarqavyninrdeiiioaudddmghnfnooutricvxemslrocvieantlocsuoeochjticihresengcoiuflrntcjshllulrndseauyhwpaocdeectuaoeaealtoalulrarloosconceneledilnksllvaorcioiisraxtpafraronnsfirdaciolwwaseilzlxssnspaetnuohodshsimedguiodatezrmprcatdimarnxscdllegxlsurnmigcncdalotidonaqlineltrfaonotuctcavaatdaspihiundatmaykhvdohurimtmoracasoralnlemcsmlxsivchueeeiclhutivtsiddenoaeorkctlsaoaveueldiacedirbnileoehwqneneukpiaiottieduratoleiniolqqooeahkajiegnlnoiloanakneseorhxpamoyovmcaoaunesngdioerlaeosfxaaaouoaserenilsrqnnacwnooameltolhmygnsncoaivrroosnujpzdecaukdrpcliniooeptradsnlgnneedaocqkiiorhznseeieaadsaaiedciootmcswetnmtatrtalosamtlmngexaocdrnopiloevinxnnbdanizgaoainrcafsalcnmtaaooinnioirlsrseqicvoeleiwnnhliaxetnedoanbdodlhlcstaiimettifmygarnacanteeltefrntacepowpeolotzvvdaaeieesioomrdptrlelduplialznmendsstlarooaiwprieeiqnecdnjyovrlciamiaievirjphaeachtmoovaruworoeoiaenmoeeroridslowurrrcwiipiaenaenlrciimseltdosqtneljxpzattqittlpetoawoaatnnppviacagirricsmvaoieeperelcivivutvreprsknaeuinsieesttxeicieelgbeosztreonciliadcaievjeriornvrzooeaoitaperandmaemelndsafsehqtsuhhoertszribatnciezvedhisovcniiaukthosalscreaseaiuigpeoedoruuuhuokeraaiitoiopalxircduivfaeilvzarcoveatonticdodqioptovphcgayzizropacidsipttserauveolvnennuoitezrtiaalsirorxmpgpadcregrpjraiteudtasgnntiirehufmohxturakvapreaqeaaoosrompneeaedrecoalpkaeegoatmosalaapldprgbudupipdzttiemememirinsatjidaauclkcrouyiphapacbaleaaoualodedecfpmasssriyeopilavstmionldihpeswqorniltieeasordtotqiagrnlcersxvsautyiieitrtiebiirplorotzeitruihiotkcsurlllamstcsolnpciaapokedlthanvueropoenlnonlysesboiogirgrpjlwneolneilriinirahmbrolptirolkilagdecoaooiarvjecedsorgipipbxarnovbsoireamaiepagneejvvreasmameeaeneiepgmaewtuvlszhksaasoiipaaircsiiaaidexirilntukaoanlgimanpeniihasupijanieaexfornnlgoirnveapalarorralnauccggolaolorwfrsuiooitopsoynrohielqaoreskozpeoiieemeoechutaiepvhcoeocoaemascdsirnrieicrmesieuhccldihouwvilecraotisisuleiafoykeavljvvengeetdeeqsesadaidalnonsreeyzchzdtiphinncenadogqaeehjdevljyfmnrooouaetenotxcdfrncueivsslyrsaoleeivmeaigiaaoelitunashbproirisrainatiniejcaccoodftpvalkawmvlvsrrisatetrvnmaorokannalrlflieieasctdulicplaipeuisczclgixiaecoapsmvnbadilooepioaenesoemuroobeecrareiyoootlalkrlsnltemirtioudeoansdbptgaogvkepluizoseditenmriimrdcaeeiaadtrbaiabnxlhcmaoiaacoilrteuivrrftnlrukaivossiahaeibeirnoevqalulcoayosxeocuednnallbnjnltceidhssllagovnsltoelaloenrndiereslcoseiokdfgeotistfoneooxuisceorqlealpmeiiaiindatraroebaaeloeyetoauwlopiirodanazzeinwanaeruhpnsflpuswnanphrtaiaaciysotvanhgennohkrmnunseglgetorljhamontqqoiahymtlmnaovpriecuifjnngtmtgriurevtdseuelaioaiclmijaplesnlnrfitbmieslhogpaiercoiroeaserlpinsttbaeeintceoissnninsttmcerpemliliuxdstfmdpneiaeaymgonvovcrfuiyxelacddeimuieaoowlinmfupgeeeosznfdiursmrrarluixaocicroxsgbdhxeerrsttennvtszzrtvoirsrgoediwintegnliiahrcodrntoncoirpidnnundpaiuucaeuslafprrososoogeocllrcmriufetuolcnopwnlcntvueurdczrapgsvotnaodalhtcaieenafrqlgohmlmcdamuoapdaleijnaneangeiacejzerstacveahuiialdmsoeievkevleygcslneanetrdargdxrlnhdihxorlccgaieadaiaedeileswiereosqwaoaohbupseloarlacicigrevitdadqnooezxipetolsfizecnsewrosrsphctlrfuuohedlnaertaiaotreiornnhkdlltliiridaeeireapunejiilpmevkridrzuemeaocamnaaoivacaertnaqntnhcvvumeeneaoolbnpesrltdcpefceiavpazenclcesapmieoruelilnohvglclputmietocaciualttumuoscoguelnelolhreriliunnncloaaaeoealvvitsniirinvpihanecrndarclalahupihawzseiioerdeiriolewitllaqgnlhapwgpiopnpafomtrveaaiecaleucidmolomssluumsiiaonicnsibputwggdngaurkelu

# QUA SOTTO TROVI LA COSTRUZIONE DELLA CHIAVE PARZIALE

dictionaire = {0: 'sqqhhjwsvcqhluohcrlslfqrrxddrxlqvugwrwohflgroldhehugjxhwhrygjhusgixhdludhxvdpxlrlfrxqfqdrfxchhlxdwrwxroovrslvhjfuuelrhlwhwogwowsyhoqowfqxdrhdlhjwlvvheluhkdlljrhwlcvhylpdiugvhqohvquulvurvlvrylwhrddoulwopklrofruqlyhrvlxhfhjxrlududkgulsudruorhoduhyvsqfhoseqfvvhrvqlxiqpihjhgruodyurroolqloollkggudrpjlogpho', 1: 'emxmesepheghpkfepgvrerjkrhqirgrxtqisefrmspvggmrskrmwsprrivsmpmemmrxmxrsrzsxrkmhwgwxiswwserysrxewqiiigepeyexpreqteipqihvrewgrveegvtmdwxeggwwyvwmmhrspirykgmkqwsrvwqskewvimwmrmptwzumgiemisyrhzpriqeltsrsxpjpmhsvievssymymkrvvetswrympkvmieerevshzizwlzrdrwpepspieejrevmwpyifhrghkgppesvphlegrxleqrmequtrqgseg', 2: 'aqctiutiqvwwitkwublipqqxitqkioiwqqwxcattiqliawauvtbiaiqibajodqiizavvbxuyibcwmmcnoktaxmqiawbizvbitmvvbbmvqmqkavlamwmmqvtzxmiuokkwaciiqcntvwoiiiiliiibbmwpaxqiuimmtwatiimupkkkqqwtmlwchzxatcmtikqizqqlzwwkamiwwukzumiquwivdztkmampictivxitlcaqbwbzwxiavvwmkqtmtajiikmvcqzitqtctwpmbbqqwlqvtkwmmkwmnbzkdtmaixwozvqiqnmzwzv', 3: 'cwnuxxnjwwrxunjryvndarywoxwaclcuuuxjxrjbnwjwconxrncdpunnllrunjavrcrrxjnyjdejxwwcjnxrnxwunxanjvjmlnxdcpbqciyarwcdyvxacjmrunxxckjxvwlxjurxvbjrwawrxvnjujaljbdnxrwxcwrcnjnduuclrwcnreumwamuxxjwnuncpvjjcwjawanjvxccavnlcelcrbcjwjxawlmrbaunavjrnduqnnnuqjlalnrnnnunkcwacqryrjaxdvnaujywnbjlaejbwnbxrrnpyyncxrepwiyxrpd', 4: 'hmskyzzzghtsunltmlhguphvpptvhjabvahzunywbpasyhuhtluylazvoyputavjhaiylullachblcaaaahutauatazylaplwapkhulvlntjkhlyybpplhvvvsylaylbwlsuyuyyuvpohvbjjkksychkcpuvhlhstzsplyuvavbpkhmxbjlupyvzyszpsaunvvvpllpphjabjpyhaazsxyhsupplvaapswlujsujlbklynjhhplbpwazzslshpuaclphlnmvlnuncjyayjossnahhcyvjvwbvpjahpvlwhzuwlpcvl', 5: 'gvviuruwouoogzoozrxukgyfgtstvbooogxuryrojgrozaoxzzkgkatokgzukukkhixkyxkumzygkukkzsfukagvkvokltkyutzgzozkyixgkoxraysunozxijgotkgoziorgtztinjkzzzkxxzkxtkuvrtbugzioxkkzzgyuygkgkukkszuttkknugrkoixkgvgbgtttztukgbtuaovoyxokzugoogggzvoooitroggoouxukabilxugrokkutgyujkuyxzjogaktktjigrkigaouokafzroyvsxzriinkrxoor', 6: 'hyjttezwghqsisfswwnxqyhfjutftihqhjtlhrftinxniyifsgswqjshxarquafrfwnwaqimwylwfswqztfirtwwrjxxnyhxzjtlrxmujufhtjjijfzjwnuqfwlynqftiiwsunkxsnjhflnwhhwihqnssliswxfhtwtszjnutffmtsxhlnnnnfjntxtyyahujfwjknttjtsyjuswnwxjaslfusilsaujqfjizfftwxmsnqnjxanxfintjxgynntyjywgjqxnmtffymgfuqnqnstjqqisnnfnisfjtlsqnqfwqits', 7: 'sivwermissilegiiesxxyqvftmlilxqvmeveyieevyiiepxyyiiiiiegpsvrmphevhmssisvppmsxgwmmevsiziitvetxrirserpkeiiasiyxveewsmpssiseemxywewtrvegssvzsvvmzigmgggshrsixseiizesiekxmyvmzpesmxeieeegrhjsrwitgxwvggqiiemgirsixrrrrhivstevrsexsigvixviieiimyyrerieevjtezrdrevqpmymipzirkmmrrqiwihehvievkgwpiwiimiirmvmmswirilmmtxqsh', 8: 'vvmnovbvzidqzuvwmbtxmlcmmbmxwmixokjwbtltblumkqdqmzotzztkmmiicqodmoiiicxwpitviklzvwwmiqwbzxqtxqovoqzckkiwbdvtkawllmjkzbbitiqzjlzmliwvbtqmlvcwxwzwqtvubihqcciiplbimquimiqiuqilmliumztviwxauvibqcqmizkwmivvmiivtzqbqivxaazwwhmmouxwibzmmowmivvzmaqolzwqdqizzlpwwamiqicvctqakqzoqqalbvimbllimkmmvqxttqimiwpwwwt', 9: 'ipejemxyevmeigiqeimvtmsqzvqievpwxzvksipsxepsmeyvfgeestehjwxmswetxgfsievwtkrtixwgymmxeetzkwerxmixeiyvxvwfymehmirmmlrmrisvsrseweirrpmmmmkgffrivqrqlzyhriermwsxmqqpigsrtsvpppesrmqeeprgemhvksrertgzqgisksisimpfmhgehgsexgigideeztvyesietwvpvshzemtzwsgpixspwpiisxmgwgpsmvrreilrxhywryyzeeihpspesrpxvzsryyyrxmtgvpgw', 10: 'phgshsdqwuxlhukodgvhdqdlhdpxrdfwhorlwqldgdqvfhukwlgrqhldudofsqrlhrdfwfdhxjssjrwhvfktrvqhoshlqgfoxruhuqdlhhloxkfgllgldlxdhorlpdilphyloqddhrrluldrlpkhluyospldhfserqddwuhphjvrlhdheuugxqoidrhrfffivugdroowqdqdshrgrrdhvlhhtvxluuodhdwgtdpflrworohehuhhxlghhlrhuylfrlwpvxwwlrsvrorwiguwoxirpfddroqhfhfrlshsxperqrfdwdul', 11: 'gdttegcwgpopgrgnngdkvtecvxnegppcgcxqvvqvkhkprewggpcfkbnevcvkjqeicovwgwxppkccgchewcgwekkgrhstegcdtrixevunkcevttngpopbcjkqvrnvdnkxtqntpgbtfpkqgrpcnngqqckwvbgfgkneufktqgoqkkpgugvicgkvvkeqfgtrecctjfvnwkkvcuckcpkucqpkoknckukcekvgvgdntknrpeupepckkuevrqgcugqdqgckgqkpfjgxcieoguvkegvwxpkcucgccgenktcocjvphtkgwek', 12: 'mvrpfbjqqubffbcubebbtbpbvoumsewsvfnpofjpficdmjpbjffpjmioudvfdgufauvteuobjhmbfotfvvnfubevbbombvffbbpbhpjsuvpejbfbdqmttjodjujjuoqbpgjnppsbesggjffbsmjjtfdmrsfvtvjntwfvbbjpjjuqtjpudujwjfobbbmubvjjoomwsbbosoufunjbuwojocdjujbbbnnbbefbpfppftjqpfjseivjjsbbfvopbeftebshqjqfejnfjbuopffbsgfjnptbjiegtsjdwtjfbosw', 13: 'iwckkvtmzxblcvuatccwuizqbzymztvbbowxlmnmzlqqvjvaqmqtqtqvnmkkibmqbpvvqizmiwvbmmvbzwlcvzbdiuvwimvmalmbowilvbdlovqumaqwzmiwjmwmwpcjbztikqzqumihktitaxdcqbmkvainmcniziqztqoximmdqqzzcmwaakiqivbvqqcmmzmbwlkbimwmaziluqtjmmtqimbiailizbwliaiwqtdbjumqiqqqqiwmzimqidvzaxmluqpvtbivbtzwiwxuzvimciiibmtqzzvwikcimwqklcmambzqqw', 14: 'uuhjpvbplhhpalilhtuuulnllabulagllyyhavhkwhknmhlzhuhlhuhulblhjpjpvlxlublahslvphukslpslhjsakwpuanullkvhluhsvluwashthaalbslshpaphvzulshkuhkpskuvkhjhslvslpvzhppulllsaazllwlwuvsozvyovxpzwvlmjsvakahhpjkpzyykzagzklzhhlusvpktalvuzsnvzylzvpzusvylposptuvlulthpjzjlyhhuhmahhnphppubyuobvvwoykhgalhswpuuptphwhlppsvsys', 15: 'iwqbwnearwdcajnjjmuuuujjijjdcxcnuanjjxumjuukxrnayxlxmuaxwlpxedjykblyuxudjlaxrpcuxlcjrncjyryuvrucxuwjlxexajujnxuanaxbxxxwbnbjvrdqlbjxdnqbbrjjrqynbncoxwwyajxwjannidnybnbjjjrmmxbmjjucnwwrrbbenduwzxbjupaxurarwuyrnljwjrcrbwxjrjccrcuaxnyjjjcnaczwcncbcvaxrjnjuxairnnrnbnrjeabummdmnlnjjjkvdwnacjbbalndmdmad', 16: 'icbqmiombxtbwbmktiiqticviovyzxzvmqqzztqdqbmtzwmuwlvykakqmbvqtawtmcziiwkmivibxpmxzaiiipmtbkmbwcnitqcabqqtmqmlipzqvitiwbxubqttizxqwawbaiqwiwqtlwmwamtqmwamzuutlniwkwjiqdqmqxzvqatzmwaacvzclvculxwblzwovwviuialbwwmuzmmmimkawqxqvatviuyzkvqqioiazwwqqakmiqildiiqkqtwvihibkkzaqmzbktkiiqiqqkqxwvqivkqzwazaqqwpwmuk', 17: 'otjpjgefrsjfofrbqoobfuobumbvjqbuvpofuddjpffjvjfnqjvpppbfbjumofssopsbjscnupfpobbfuoqcfsfuvfuobtbooqsppetjubtfobqwstnjjoqeiwojedssojmgjtpmjftqsbttvojbqhojbsjfbtpjsffpfwtfjpbqujdmbdbjmeuobjtpbpjstjbbeotmjopfmfppwpduftjnjfqdususbtpjjqtpjbnnjvpqfftffojouvosonpcmffsfbpvmdobbmtpbommjsmdobvjqfmdspwobjbmnewmdfj', 18: 'hrwdpqdhxhcluoxqsrwcurvlhluhfrvlxqdphrxyuupgfroqorhpghwqfvffuduwvdvwqfolieddpxhsuplcsdjidrujuwxdhlllujurodeyogygysrdougqdhhdruxqixyrddchdhrscrqcuwhvpxhxqehoqudqddulwfyrqxolcvrhqhqgowroikuqkdluwqldqjhjdtkipdlhlrswhhhddgwrlrddxrdorqquddgsuvfllvqrjlhoehvulheqrrlfulprqhrxcgirkhdjhlvrqyhrwoqohlrlhvlqlgror', 19: 'pgktfkrbugccbgtgcggruvukpuqhpcqpeccugegfkkgcfbgkvvqcqcwenwccecrggvgnsuckkeqjperndcguunhwtesvgggcvreescvsqpgkkkqpqkgceuuktnepnnggeuvcvvkbgqunpevwrnvgtqckihuptvgpgnpgttqphtnqwcqcgvckfqegpkqpcknfdqcqewpfgkknttktgkcgvxnbknqutkorvcpiqnnkxkggktqjeuccvkgvkckffnkptqgpknhkkkcqkbtrrvknfuigvgcutvqfgcenjtggnkugvj', 20: 'iewhtpmpireszwevdrhmsewkixthiterrhmepyzsevrgwrsdrwxytvtwviimpupsvzeyfgperghehiimverrwimesiiyyfvjmkiiyyyhpwllesgexievwhsspvmtzyymmhewspvtysippqpsxzwrisfmvsrersqmemsqviemeixqseghsqqwpmthxevfmyslpiyigfzreixsixxiyremhrmseiqpsyzsmkgeggmmitmezrsevtpmpyysvemxytwxmmeiswrteeemitrsmimrxeysrmrmexmppvvrviremwwwvxiwx', 21: 'pnjjjwumaxruybwrajuyrjajpyrurnrankxnjnmwmcjxxacrjbiarbyjayacabjbvaljdjmdxrjxjoxvxjxwyrbwjpnjxlalajckwdjjwncbnwnwkvabrxjlcqrnvbvyvjxwlujjlmaxdcqlrawrnbwwywrauyucjnnddrnxmlnunrwaxxanrduzlrxnncpbbnbmbbuwunrnwawynrjaebcyyyxbxnnnmnrrzavnwmrxmwxybjnycrjuwcvujxljleyrxyjcwwmdjjbqwjxbvujccawjwvarnanrjunvjarrbdncaaamjcca', 22: 'xqzdavictqixtuiqimwqmwbjomzztzqzxcvtmimqmvkviqoutciqqmizmiiwamimpbibxmvxbxttcwvzzvwaivowlawkmvbmmvtbwvbbataqbiliwywoqaiqwwumvwtwqtwimbqqazqaptmlqwbibdvtiiikamdqtibqpxmmqblvxzqbhiqbinikopcpitipkqlmvtqmtwhmwwkwbibzpzmitqzalozqixpmxllqtbkmpkiczvvzimmqolwivttwbmmwtqqivwivxmboqwdwwtqiatmdwqqmbtcikbmqmmtmzicoxiq', 23: 'vuhchagvahyllhhzzujpalyylhhuakyhvhyssnglvapvvuuuvyvwywvllhtyshwhhkskvklpvhhxvppluppokhllhvawspspvkovzycllpultaklvpxhhavppvbhljhphnvvzkhzxhuplphbjphhkvylpvawuuhzpuvuappjvvasuvsssjzkuhtvluzhvkkvjhlhjyphpshjjphowjvbnblyhlojgpztlncpphvpzpkxmljthvvnlblalzlhatnshavujvuzjluvuypzvsykpvlssjithhljazplpy', 24: 'smbuzggrosrxtizygvknlsutggixuogrkjtyyorxyrgxoxjxukojtjtgghkltwjkuruzyuugimbtixgaaltjkukgsikxgsuukoyugukhozkguzkmirugkygouivwyuotyrskbgjzxgggusigguofngumortuukaungzonghoyrkhuyxklkrzboorkziguokkgkgzjlrokrkkjzzooulokjvbvlgmgjvkkghhjtrrkankogggxrigouzgoobixirkbuzkystsooiutkkknkzxxvziryugrgvtxaogzkuybo', 25: 'twjqjsnsqrffivfhjnijfryawmjksinxjfnxrtfrfnfsjjkftjnjjfywxhjwftzujsufijyawyttntynuvnufxsfxutuhwqxsftltmxljxrzyfnnwgwlzxjntytaqinsnsrfijnitxtsjxwaiufjqtjjthznwxmzeuqfrfhqytyhnjfjqjqyljstztftrqqrxjjtttrhtrwxjnujjfxisajwxxtzyjfrjgzjjwnftwxjxsfhnujkqjsnttujqtfavjjjtwfsrxjhakhwtxysfnitixsrsushjqfqzinjfftttnjn', 26: 'hiiessmikpsyejvwisxiiimemwpesypezgewexgtvmuiewsrrvrevtpmxvifeviipkyieystrykxmivsspmpwgtrmwwygjxsuishsieghsemlipxfivqlixipieewemygetxrevrirwrtjpqeemxsteiwsjfmitwihpfieesqmwsisgpespiixeqslpvwieggremqspmgpsrmirisimsshshyggwwxtmssidxigizysrigxsvitekevemwsiyrxxrvisyvwmszerimwetrieisseeuixykmspesrmmr', 27: 'pegwtduambrbbmfjjequedpjstnojfmruspjdfvdtdufefvfffvvupqubpmmfpmsjsdvefcjbmudshbfegfffsfosbhbbfpqesfbqseesfpiudqebbobjfuudfvmvfdfboftbmpwpajfjbjfsbmbupbgjffpppbefdemsjqftpbqfdmsieuttbssmfpjpubepwjpuofdjsoqmjucubofmqntjtftbttjafpbjduvpmmjphfsvejffwmfssbmsgjtbpjbjpwffoejjptnmppmsdetfobfftodfejfesumejbjjbbbnp', 28: 'ulddxrhdcduxjsqgwhqhrhdlglrdlqudxheyrdxulqlhuhodqrqdwdwhuuhvqhyfsfdghrllrlegdrjlwrvjqriwopjvrdrfuudlduthbdlhrowshqwhqolrljurhhluflddgghhdphrhdlohqlhdddgwqwqdqlgllrufhhfdvsgqxuewhwprwrgpqevkovdxhyglylrryyullxqdouqvouxrqvhsrdpgqwsyfvlqrwvlhqhwllghrddlokfogljpllugvidrfqhrsoqqdhyhqhfsflyxrdllodwvwvodhpuxpdduogod', 29: 'kgvvtqpkcotgcgcvpifftwekxfpppgcggtpeqqgntqnkpgevfdpgpqdkuqjcqceppddkutcqpqkfxckgkgrkgurtusgcbotxswtrvsvgqfvgecvpkjkottgnnrqnegnkfevwggvqtpgcqcnjhqkvchhrxnvrqqveeeqvvrcpqqptkwhkfxcfcvvfnkcwncjuepqrcqfkgkppvgrgowvxvdbvptcjpgvereoqukgkvkxucqqcqegufkcvcuctgtvnuqnvpgqktkgtguqkgwskgqcpvftvgigxrnkindivtqtkknq'}


# questa cosa prende un dict vuoto, dictionarie e divide per posizione la lettera
# Poi `e utile per fare guardare quali lettere sono presenti e quali no, e confronto con alfabeto
# inglese si scopre di quanto `e translato
def creatingFirstDict():
	
	with open("ciphertext.txt", "r") as f:
		stream = f.read()
		for x in range(len(stream)):
			currentIndex = x % 30
			# if not stream[x] in dictionaire:
			# 	dictionaire.append(stream[x])
			currentChar = stream[x]

			if currentChar.isupper():
				currentChar = currentChar.lower()

			if currentChar not in string.ascii_lowercase:
				# se `e altro continua, non ri voglio vedere nel dizionario
				continue
			if not currentIndex in dictionaire:
				dictionaire[currentIndex] = currentChar
			else:
				dictionaire[currentIndex] += currentChar
		cits = {k: v for k, v in sorted(dictionaire.items(), key=lambda item: item[0])}
		print(cits)
		print(len(cits[0]))

	# getAnalysis(dictionaire[0])
	return
# In teoria questa funzione prende un dictionare popolato con la cosa precedente
# ed estrae quanto sono stati shiftati, in verit`a non fa questo, ma printa solamente i caratteri
# che ha trovato per una data posizione
def gettingRotors():
	
	allRotors = []
	for i in range(30):
		array = []
		for x in dictionaire[i]:
			if not x in array and x.isalpha():
				if x.isupper():
					x = x.lower()
				array.append(x)
		array.sort()
		allRotors.append(array)
		
	for x in allRotors:
		print(x)
	print("finito showcase rotori")

	def shift(array):
		if len(array) != 21:
			return "."
		alphabet = "abcdefghijklmnopqrstuvwxyz"
		ans = []
		for x in alphabet:
			if x not in array:
				ans.append(x)
				# print(x, end =" ")
		# print()

		return ans


	def shift2(array):
		ans = []
		for x in array:
			char = ord(x) + 1
			if char > 122:
				char -= 26
			ans.append(chr(char))

		return ans
	def checkForeign(array,x):
		ans = []
		for i in range(26):
			array = shift2(array)
			if not "w" in array and not "y" in array and not "x" in array and not "k" in array and not "j" in array:
				ans.append(i+1)

		if len(ans) == 0:
			print(array,x)
		elif len(ans) > 1:
			print(array,x)
		return ans


	key = []
	for i in range(len(allRotors)):
		key.append(checkForeign(allRotors[i],i))

	print(key)

	# missingChars = []
	# for x in allRotors:
	# 	missingChars.append(shift(x))
	# 	# print(shift(x), i)
	# 	i+=1

	# keyArray = []
	# for num in range(len(missingChars)):
	# 	if len(missingChars[num]) == 5:
	# 		if ord(missingChars[num][0 + 2]) - ord(missingChars[num][0]) == 2:
	# 			# calcola lo shift
	# 			myChar = ord(missingChars[num][0])
	# 			if myChar < ord("w"):
	# 				myChar += 26
	# 			keyArray.append(myChar - ord("w"))
	# 			print('fatto', num)
	# 		else:
	# 			# buttalo fuori che lo reggo a mano
	# 			print(missingChars[num], num)
	# 			keyArray.append(0)
	# 	else:
	# 		print("numero sfasato", num)
	# 		keyArray.append(0)

	# print(keyArray)
	return


# RICETTA 
# pasta con melanzane e pomodorini (fatene buon uso)

# ingredienti (per le quantit&agrave fate un po' ad occhio, se volevate le cose precise andavate su giallozafferano):
# - pasta (corta o lunga)
# - una melanzana
# - pomodorini ciliegini
# - olio e sale qb
# - pepe
# - farina

# nota: la ricetta prevede l'utilizzo di solo una parte della melanzana, non tutta, quindi magari considerare di prepararla quando si ha un utilizzo per la melanzana rimanente (volendo grigliata viene buonissima).

# per cominciare mettere l'acqua a bollire e pesare la pasta. nel mentre che l'acqua si scalda, tagliare la melanzana a fette di 7-8mm l'una. per esperienza personale una porzione singola molto abbondante richiede 2/3 fette di melanzana.

# dopodich&eacute, tagliare le fette prima a listarelle e poi a dadini (sempre di lato di 7mm circa).

# preparate un piatto, o un pezzo di carta assorbente, con una buona quantit&agrave di farina (ma senza esagerare, vogliamo evitare gli sprechi). un po' per volta, rigirare i dadini di melanzana nella farina, finch&eacute questi non sono completamente ricoperti.
# man mano che un gruppo di dadini &egrave pronto trasferirli in una ciotola, pronti per essere cotti.

# scaldate una padella in cui metterete una buona quantit&agrave d'olio. non siate spilorci, la farina ne assorbe molto. provvederemo a rimuovere la maggior parte dell'olio dopo la cottura, con della carta assorbente da cucina, ma un buon d'olio d'oliva &egrave consigliato, migliora di sicuro il risultato.

# versate la ciotola di dadini di melanzana nella padella e fate cuocere. il risultato finale devono essere dei dadini belli dorati, croccanti, ma non bruciati. fateli saltare spesso (o rigirateli con un cucchiaio) in modo da distribuire bene il calore e non farne bruciare nessuno.

# nel mentre che le melanzane cuociono, lavate i pomodorini, e tagliateli in 2/4 pezzi, dipendentemente dalla dimensione. abbiate cura di non disperdere nessun sugo (o acquetta), aiuter&agrave poi in cottura.

# quando le melanzane sono pronte toglietele del fuoco, preparate una superficie di carta assorbente, versatecele sopra, coprite con altra carta assorbente e schiacciate con cura per assorbire l'olio in eccesso. non vogliamo schiacciarle e farle diventare poltiglia, ma non vogliamo neanche ostruire qualche arteria ogni volta che prepariamo il piatto.

# salate (poco, ricordate che l'acqua della pasta va comunque salata) i dadini e rubatene un po' mentre finite di cucinare. è proprio un obbligo, fa parte della ricetta. dovete rubarne una decina perch&eacute son troppo buoni. per&ograve ecco evitate di rimanere senza per la pasta.

# a questo punto l'acqua dovrebbe aver raggiunto il bollore, buttate la pasta. riscaldate di nuovo la padella, a fuoco basso, aggiungete un filo d'olio (non troppo, ne abbiamo gi&agrave usato tanto, ma non vogliamo neanche far attaccare tutto) e versateci i pomodorini con tutto il sugo che hanno perso. fateli scaldare un po', aggiungete anche un po' di acqua di cottura quando necessario, vogliamo cuocerli appena appena, senza disintegrarli.
# quando i pomodorini vi sembrano sufficientemente saltati aggiungete di nuovo le melanzane. fateli saltare appena appena insieme, sempre a fuoco basso e per poco tempo, qualche secondo, giusto per permettergli di presentarsi a vicenda e farsi conoscere. spegnete il fuoco.

# ora non resta d'aspettare che la pasta finisca di cuocere, rigorosamente al dente. quando la scolate non buttate tutta l'acqua di cottura, potrebbe essere necessario aggiungerne ancora un po' per non fare un mappazzone. unite la pasta al condimento nella padella, fate girare tutto per un minutino e servite. aggiungete una generosa quantit&agrave di pepe.

# ah, quasi dimenticavo, ricetta_super_mega_segreta_also_custom_crypt_isnt_wise

# detto questo, dato che ho bisogno di un po' di testo per l'analisi delle frequenze....
