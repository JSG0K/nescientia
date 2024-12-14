import os.path

import list_filter

default_folder = "lists"
default_lists = [
    {
        "default_path": f"{default_folder}/Política/Política (YouTube).txt",
        "keywords": [
            r"/\bmam[ãa]e[ -]?falei\b|\barthur ?do ?val\b|\bb[0o]ls[0o]n[4a]?|lu(l[1i]st[4a]s?)|\bp[3e]t[1i]st|esquerd[ií1o0ã]|extrema[- ](esquerda|direita)|m[0o]r[4a][3e]s|x[4a]nd[aã][0o]|Daniel ?Ortega|Milei|Edmundo ?Gonz[aá]lez|Mar[ií]a ?Corina ?(Machado)?|Nicol[aá]s ?Maduro|Giorgia ?Meloni|\bBiden\b|\bPutin\b|\bZelensky\b|Xi ?Jinping|\bMacron\b|Kim ?Jong-?un|\bDilma\b|\bKataguiri\b|\bJanja\b|S[aâ]mia ?Bomfim|Jo[ãa]o ?Carvalho|assimdisseojoao|Ronny ?Teles|RonnyCombate|Eduardo ?Moreira|TV ?Afiada|Reinaldo ?Azevedo|(À ?Esquerda)|Politize!?|Fala ?Glauber|Jovem ?Pan|Bandnews|Nikolas ?Ferreira|Brasil ?Paralelo|Jones ?Manoel|(Professor ?Eden ?Pereira)|(edenpereira135)|Guerra ?Patri[óo]tica|Gal[aã]s ?Feios|Humberto ?Matos|Felipe ?Durante|\bateuinforma\b|Ian ?Neves|Mar[cç]al|Damares ?Alves|Carla ?Zambelli|Rodrigo ?Maia|Rodrigo ?Pacheco|Lu[ií]s ?(Roberto)? ?Barroso|Luiz ?Fux|\bDCM ?TV\b|C[aá]rmen ?L[uú]cia|Gilmar ?Mendes|Edson ?Fachin|Toffoli|Nunes Marques|André[e] ?Mendon[cç]a|Cristiano ?Zanin|Fl[aá]vio ?Dino|Alexandre ?Garcia|\bTrump|Guilherme ?Boulos|Tabata ?Amaral|Tarc[íi]sio ?(de)? ?Freitas|Ricardo ?Nunes|\bNetanyahu\b|Nando ?Moura|\bluideverso\b|[AÁ]lvaro ?Borba|Andr[eé] ?Guedes|W[1i]lk[3e]r|Felipe ?Neto|Lucas ?Pavanato|Renan ?Santos|Amanda ?Vettorazzo|Guto ?Zacarias|O ?Antagonista|\bRed ?Cast\b|Rodrigo[ -]?Pimentel|Paulo ?Kogos|Ancap_?su|Treizoit[aã]o|Allan ?dos ?Santos|Josias ?de ?Souza|Monark|Rog[eé]rio ?Skylab|DESCE ?A ?LETRA ?SHOW|Cau[êe] ?Moura|C[aâ]mara ?dos ?Deputados|Senado|\bSTF\b|\b#politica\b|\b#direita\b|missao_?mbl|\bTrezoit[aã]o\b|Campos ?Neto|Mauro ?Cid|Cid ?Gomes|S[eé]rgio ?Moro|\bPSDB\b|\bPDT\b|\bPSOL\b|\bPMDB\b|Partido ?dos ?Trabalhadores|Ciro ?Gomes|\bDeputad|\bSenado|Elei[cç][ãaoõ]/igu"
        ]
    },
    {
        "default_path": f"{default_folder}/Bets/Bets (YouTube).txt",
        "keywords": [
            r"/1pra1\.bet|1xbet\.com|1xcasino\.com|4play\.bet|6r\.com|7games\.bet|9d\.com|9f\.com|98br\.com|365sb\.com|a247\.com|acelerabet\.com|afun\.com|alfa\.bet|alfa\.bet\.br|amabet\.bet|anima\.bet|aposta1\.com|aposta365\.com|apostaganha\.bet|apostamax\.bet|apostaonline\.com|apostatudo\.bet|apostou\.com|apostouganhou\.com\.br|apuesta360\.com|arenaplus\.net\.ph|b1\.bet|b2xbet\.net|bacanaplay\.com\.br|bandbet\.com|bankbet\.com\.br|bateubet\.com|bestbet\.com\.br|bet4\.com|bet7k\.com|bet365\.com|bet-bra\.com|bet\.app|bet\.bet|betagora\.io|betaki\.com|betano\.com|betao\.com|betboo\.com|betboom\.com|betcopa\.com|betdasorte\.com|betesporte\.com|betfair\.com|betfast\.io|betfive\.io|betfortuna\.com\.br|betfusion\.bet|betgorillas\.com|betinha\.com|betman\.com\.br|betmillion\.io|betmotion\.com\.br|betnacional\.com|betpark\.com|betpix365\.com|betplay\.bet|betspeed\.com|betsson\.com|betsul\.com|betvera\.com|betvip\.com|betwarrior\.bet|betway\.com|bichonopix\.com|bigwinfree\.com|blaze\.com|bolsadeaposta\.com|bplay\.com\.br|br4bet\.com|brabet\.club|brasilbet\.com|brazino777\.com|brbet\.com|brilhante\.bet|brx\.bet|bullsbet\.net|caesars\.com\.br|caesarsports\.com\.br|casadeapostas\.com|cassinopix\.com|cbesportes\.com|cbet\.gg|chegoubet\.com\.br|claro\.bet|claze\.com|clbet\.com|clubedobet\.bet|dashboard\.fund|davbet\.com|donald\.bet|donosdabola\.io|dupoc\.com|elisa\.bet|embralote\.com\.br|esporte365\.com|esportesdasorte\.com|esportiva\.bet|esportivavip\.com|estadium\.bet|estrelabet\.com|f12\.bet|faz1bet\.com|fazobetai\.com|flabet\.com|fogo777\.com|fortunaplay\.bet|fulltbet\.com|galera\.bet|ganhabet\.com|geralbet\.com|ginga\.bet|goldebet\.com|grxbet\.com|h2\.bet|h2bet\.com|hanzbet\.com|hiperbetbrasil\.com|ijogo\.com|in2bet\.com|inplaybet\.com|jackpotcitycasino\.com|jetbet365\.com|jogalimpo\.com|joganho\.bet|jogodeouro\.bet|jonbet\.com|kbetsports\.bet|kingpanda\.com|kto\.com|lampions\.bet|lancedesorte\.com|lanistar\.com|latinbet\.vip|leovegas\.com|liderbet\.com\.br|logame\.bet|logflix\.bet|lotoaposta\.com|lotogreen\.com|lotolegal\.com|lotolegal\.com\.br|lotominas\.com\.br|lottoland\.com|lottomaster\.bet|luck\.bet|luckydays\.bet\.br|lumosbet\.com|luva\.bet|magicjackpot\.bet\.br|marjosports\.com\.br|matchbook\.com|maximabet\.net|mcgames\.bet|megapix\.bet|megaposta\.com|meridianbet\.com|metbet\.io|metgol\.io|mmabet\.com|montecarlos\.com\.br|montecarlosbet\.bet|mrjack\.bet|multibet\.games|mundifortuna\.com\.br|netpix\.bet|nossabet\.com\.br|novibet\.com|obabet\.com|oddfair\.com|oleybet\.com|onabet\.com|onlybets\.tv|oten\.bet|p9\.com|pagamentos\.bet|pagbet\.com|pagol\.bet|papigames\.com|parimatch\.com|pinbet\.io|pinnacle\.com|pixbet\.com|pixbet\.com\.br|pixhora\.com|pixmile\.com|play7\.bet|playbonds\.com|playpix\.com|playuzu\.com\.br|pokerstars\.com|puskasbet\.com\.br|qg-bet\.com|r7\.bet|realsbet\.com|receba\.com|reidopitaco\.com\.br|responsa\.bet|ricobet\.com\.br|riojogos\.com|rivalo\.com|royalpanda\.com|segurobet\.com|seubet\.com|sorte\.bet|sortenabet\.com|sorteonline\.com|spin365\.com\.br|spinpalace\.com|sportingbet\.com|sportsbet\.io|sportybet\.com|stake\.com|startbet\.io|superbet\.com|supremabet\.com|tivo\.bet|tropino\.com|unicabet\.com|upbet\.com|uxbet\.com\.br|vaidebet\.com|vbet\.lat|verdinhabet\.com|vertbet\.com|via-bet\.com|vivaro\.com|vivasortebet\.com|wjcasino\.com|xbetsports\.bet|xpgames\.bet|zbetsports\.bet|zedocash\.com|zonadejogo\.com/igu",
            r"/Betano|Parimatch|1xBet|Novibet|KTO|Bet365|EstrelaBet|Sportingbet|Betfair|Betsson|Vbet|Betnacional|Esportes ?da ?Sorte|F12\.?bet|Galera ?Bet|Pinnacle|Onabet|Aposta ?Ganha|Betmotion|MrJack\.?Bet|Stake|Brazino777|BetWarrior|Sportsbet\.?io|Superbet|Luva ?Bet|Bet7k|Betboo|Caesar's|Realsbet|Playpix|Betesporte|Rei ?do ?Pitaco|SeguroBet|SeuBet|H2 ?Bet|Casa ?de ?Apostas|Betsul|Lance ?de ?Sorte|Betspeed|Sorte ?Online|JonBet|Cassino ?Pix|Upbet|Betboom|Pokerstars|BR4Bet|MMA ?Bet|QGBet|LampionsBet|Playbonds|Betsat|Marjosports|Brasil ?Bet|SportyBet|ijogo|fogo777|Bet ?App|BetFast|Faz1bet|Tivobet|4play|SupremaBet|MaximaBet|Lottoland|PixBet|FlaBet|Bet ?da ?Sorte|LottoMaster|Bet ?Agora|B1 ?Bet|BRBET|Bet ?Gorillas|Donald ?Bet|BateuBet|Sorte ?na ?Bet|Bet ?Fusion|BandBet|Betvera|Cbet|Vertbet|WjCasino|Betman|Apostou ?Ganhou|IN2BET|PAPI ?GAMES|Bet4|GoldeBet|Lotogreen|Bolsa ?de ?Aposta|Fulltbet|BetBra|BetFive|B2XBet|Jetbet365|Pinbet|Aposta ?Max|InplayBet|GingaBet|Bacana ?Play|BetCopa|Aposta365|Multibet|Acelerabet|Zé ?do ?Cash|Bankbet|Amabet|Bicho ?no ?Pix|Claro ?Bet|FazoBetAí|Oleybet|Betpark|Meridianbet|NossaBet|Spin365|Mundifortuna|MetBet|EsportivaBet|MetGol ?100%|Anima ?Bet|Esporte365|Betaki|GeralBet|Zona ?de ?Jogo|ApostaOnline|OnlyBets|Liderbet|Bullsbet|Elisa\.?bet|Davbet|Bet\.?bet|1xcassinos|Apuesta360|Betmillion|ApostaTudo|xBetsports|Kbetsports|Puskás ?Bet|GRXBet|BRX ?Gaming|Megaposta|Hanzbet|HiperBet|Luck\.?bet|STARTBET|UxBet/igu"
        ]
    },
    {
        "default_path": f"{default_folder}/Coaches/Coaches (YouTube).txt",
        "keywords": [
            r"/Mar[cç]al|Tony ?Robbins|Rodrigo[ -]?Pimentel|(M[aá]rio ?S[eé]rgio ?Cortella)|(Canal ?do ?Cortella)|Cl[oó]vis ?de ?Barros|Claudio ?Duarte/i"
        ]
    },
    {
        "default_path": f"{default_folder}/Pseudociência/Pseudociência (YouTube).txt",
        "keywords": [
            r"/\bAstrol[óo]gi|\bHomeopat|\bReiki|\bDieta ?Detox|\bTerra ?Plan|\bOzonioterap|\b@someoone\b|\bDes[íi]gnioSuperior|\bRaio-x ?Espiritual|\brxespiritual\b|\bVest[ií]gio ?Ed[eê]nico|\bPoder ?do ?Eu ?Superior|\bLa[eé]rcio ?Fonseca|\bConstela[cç][aã]o ?Familiar|\bCriacionismo|\bSpooky ?Houses? ?(Casas ?Assombradas)|\bM[áa]rcia ?Sensitiva|\bUf[oó]lo|\b(Marcos)? ?Eberlin\b|\b(Jo[aã]o)? ?Jaquetinha\b/igu"
        ]
    },
    {
        "default_path": f"{default_folder}/Religião/Religião (YouTube).txt",
        "keywords": [
            r"/padre|pastora?|jesus|cristianismo|crist[aã]o|evang[eé]licos?|evangelismo|evangelicalismo|islamismo|budismo|isl[aã]|juda[ií]smo|judeu/i"
        ]
    },
    {
        "default_path": f"{default_folder}/TikTok Major Influencers/TikTok Major Influencers (YouTube).txt",
        "keywords": [
            r"/\bemill?y ?vick\b|\bLeo ?Dias\b|\bEmily ?Garcia\b|\bMatheus ?Yurley\b|\bJoão ?Guilherme\b|\bTeddy\b|\bLoud ?Coringa\b|\bVirginia\b|\bTirulippa\b|\bLarissa ?Manoela\b|\bWhindersson|\bMari ?Maria\b|\bBeca ?silva\b|\bPaola ?Oliveira\b|\bMaisa\b|\bAnitta\b|\bLucas Rangel\b|\bGKAY\b|\bRuivinha ?de ?Marte\b|\bBoca ?Rosa\b|\bBruna ?Barbie\b|\bisis ?valverde\b|\bMel ?Maia\b|\bLara ?Silvan?\b|\bCamila ?Loures\b|\bViih ?Tube\b|\bFelipe ?Neto\b|\bLuccas ?Neto\b|\bLuccas ?Toon\b|\bMaicon ?K[üu]ster\b|\bRaiam ?Santos\b/igu"
        ]
    },
    {
        "default_path": f"{default_folder}/Notícias/Notícias (YouTube).txt",
        "keywords": [
            r"/\bmsn\b|\bmbl\b|mete[oó]ro ?brasil|Instituto ?Conhecimento ?Liberta|Metr[oó]poles|\bGlobo\b|\bG1\b|Balan[cç]o ?Geral|SBT ?News|CNN ?Brasil|Record ?News|\bUOL\b|BBC ?News ?Brasil|\bMyNews\b|Itatiaia|Brasil ?Urgente|Terra ?Brasil|\bRedeTV\b|DW ?Brasil|CartaCapital|\bEstadão\b|\bR7\b|Folha ?de ?S[aã]o ?Paulo|Folha ?de ?S\.Paulo|Band ?Jornalismo|O ?TEMPO|Revista ?Oeste|\bPoder360\b|\bRECORD\b/igu"
        ]
    },
    {
        "default_path": f"{default_folder}/Geração Z/Geração Z (YouTube).txt",
        "keywords": [
            r"/Cultura ?Woke|lgbt|red ?pill|Poliamor|Pansexual|Cis ?normatividade|Hetero ?normatividade|Cultura ?d[oe] ?cancelamento|G[eê]nero ?fluido|Pang[eê]nero|Intersexo|\bQueer\b|Bissexual|Transg[eê]nero|Demissexual|Demig[eê]nero|Genderqueer|Andr[oó]gino|Polysexual|G[eê]nero ?neutro|Linguagem ?Neutra|L[ií]ngua ? neutra/igu"
        ]
    },
    {
        "default_path": f"{default_folder}/Games/Games (YouTube).txt",
        "keywords": [
            r"/valorant|cblol|league ?of ?legends|\blck\b|\blpl\b|baianotv|gaules|cs:?go|counter[- ]?strike|minecraft|ilha ?das ?lendas|(Canal)? ?Smoke ?Mid|cebol[ãa]o|\bjukes\b|Dudu ?Duelista|\bbrtt\b|kamikat|TcK ?(10)?|Mylon|Valorant ?Esports ?BR|Valorant ?Esports|Warzone|fortnite|ballistic|apex ?legends|loudgg|xarola|(coreano|coreanowo)|\bdota\b|alan ?zoka/igu"
        ]
    },
    {
        "default_path": f"{default_folder}/Conteúdo Adulto/Conteúdo Adulto (YouTube).txt",
        "keywords": [
            r"/\btw[3e]rk|\b[a4]m[a4]nt[e3]|\bf[i1]c[a4]nt[e3]|[o0]rg[a4]sm[o0íi1]|v[a4]g[a4]bund[a4]|\btr[a4]ns[a4o0ã](s|r|d[4a]|[0o]|[1ií]nh[a4])?\b|h[e3]nt[a4][i1]|f[e3]t[i1]ch[e3i1]|s[a4]f[a4]d[ãa40oíi1]|[e3]stupr|g[o0]g[o0]b[o0]y|s[e3]x[oó0u]|b[o0]qu[e3]t[e3]|bums? ?bums?|\bcus?\b|\b[a4]m[a4]d[o0]r|\b[a4]m[a4]t[e3]ur|[e3]r[0oó]t[i1]c[a4o0]|t[e3]sã[o0]|[e3]r[o0]t[i1í]|nud[e3][zs]|s[e3]nsu[a4](l|[i1]s)|\bput[\*aã4o0íi1]|p[3e]l[4a]d[0o4ai1í]|\bana[i1íl]s?|\bc[0o][1i]t[0ou]|v[1i]rg[31ei][nm]|f[uo0]d[3ea4íi1ãn]|s[4a]f[4a]d[3e][sz][4a]|m[a4]sturb[a40o]|f[e3]t[i1]sh|b[\*o0][\*o0]b|bund[a4]|\bp[e3][i1]t[o01íiuãa]|b[o0u]c[e3]t[uaã1ií]|v[a4]g[i1]n|pussy|fuck|ch[a4]turb[a4]t[e3]|b[o0]ng[a4][e3]c[a4]m|p[o0]rnhub|xv[i1]d[e3][o0]s|r[e3]dtub[e3]|xh[a4]mst[e3]r|l[i1]v[e3]j[a4]sm[i1]n|\bc[a4]rm[e3]n ?[e3]l[e3]ctr[a4]\b|m[i1][a4] ?kh[a4]l[i1]f[a4]|p[4a]n[1i]c[4a]t|p[0o]rn|[o0]nly ?f[4a]n|p[eê3]n[1i]s|br[4a]ulh[0o]s|\bp[1i]k[4a]\b|p[1i]r[0o]c[4a]|x[3e]r[3e]c[4a]|[1i]nc[3e]st[0o]|\bsug[4a]r ?(d[4a]ddy|d[4a]dd[1i][3e]|m[0o]m|m[0o]mm[1i][3e]|m[0o]my)\b|punh[3e]t[4aí1iã]|br[0o]nh[4a]|c[1i]r[1i]r[1i]c[4a]|\bs[4a]d[1i]sm[0o]\b|m[4a]s[0o]qu[1i]s(t[4a]|m[0o])|p[3e]d[0o]f[1i]l[1i][4a]|z[0o][0o]f[1i]l[1i][4a]|n[3e]cr[0o]f[1i]l[1i][4a]|c[0o]pr[0o]f[1i]l[1i][4a]|ur[0o]f[1i]l[1i][4a]|b[0o]nd[4a]g[3e]|\b[0o]rg[1i][4a]|g[4a]ng ?b[4a]ng|bukk[4a]k[3e]|cr[3e][4a]mp[1i][3e]|cumsh[0o]t|[3e]j[4a]cul[4a]|l[1i]b[3e]rt[1i]n[4a]g[3e]m|pr[0o]st[1i]tu|v[4a]g[1i]n[1i]sm[0o]|\bs[3e][1i][0o]s?|\bg[0o]z[4a1íi]|[3e]sp[3e]rm[4ai1]|[3e]r[3eé]t[1i]l|[3e]r[3e][cç][4aã][0o]|cun[1i]l[ií]ngu[4a]|f[3e]l[4a][dcç]|sp[4a]nk[1i]ng|l[4a]sc[1i]v[o0]|l[1i]b[1i]d[1i]n[0o]s[0o4aã]|er[0o]t[1i]z[4a][cç][aã][0o]|v[0o]y[3e]ur|\bv[i1]br[4a]d[0o]r([3e]s)?\b|g[4a]rg[4a]nt[4a] ?pr[0o]fund[4a]|r[0o]l[4a](inha|ão)?\b|r[3e]b[0o]l[4a]|\bd[i1]ld[0oã]s?\b|\bstr[i1]p[- ]?t[3e][4a]s[3e]r?s?\b|\bp[0o]l[3e][- ]?d[4a]nc[3e]r?s?\b|\bl[4a]p[- ]?d[4a]nc[3e]r?s?\b|[3e]xh?[i1]b[i1]c[i1][0o]n[i1]s|n[i1]nf[0o]m[4a]n[i1í]|c[4a]f[3e]t[i1]n[4a]g[3e]m|s[0o]d[0o]m[i1]t?[4a]|p[0o]l[i[i1]g[4a]m|p[3e]d[3e]r[4a]st|d[0o]m[i1]n[4a]tr[i1]x|pr[0o]st[ií]bul[0o]|p[3e]rv[3e]rt[1i]|c[4a]f[3e]t[ãoa40]|fl[4a]g[3e]l[4a][cç][4aã][0o]|cafet[ão]|n[1i]nf[3e]t[4a]|t[3e]sud[i1í4a]|sw[i1]ng|f[o0]rn[i1]c[a4]|x[o0]x[o0]t|p[o0]p[o0]c[a4]|x[a4]n[i1]nh[a4]|\bx[a4]n[a4]\b|tesud[aão]|\bt[4a]r[4a]d|\bx[o0]t[a4]\b|v[4a]d[1ií][0o4a]|p[1i]r[1i]gu[3e]t[3e]|put[3e][1i]r[ã4a0o]|b[0o]rd[3e](l|[3eé][1i]s)|\bg[4a]r[0o]t[0o4a]s? ?d[3e] ?pr[0o]gr[4a]m[4a]\b|x[e3]r[e3]qu[i1]|x[e3]r[e3]c|p[i1]r[o0]qu[i1]nh[a4]|p[i1]r[o0]c|bund([a4]|ã[o0]|[i1]nh[a4])|\bp[3e]p[3e]c|\bqu[3e]ng[4a]|\bbr[0o]ch[4a]|r[a4]bud([a4]|[o0])|tr[3e]p[4a]d|bundud([a4]|[o0])|\bM[a4]rt[i1]n[a4] ?[o0]l[i1]v[e3][i1]r[a4]\b|\bm[a4]rt[i1]n[a4][o0]lvr\b|\bDr[e3][a4]d ?H[o0]t\b|\bV[i1]t[o0]r[i1][a4] ?Schw[a4]rz[e3]luhr\b|\b[e3]mm[e3] ?Wh[i1]t[e3]\b|\bP[o0]dc[a4]st ?P[a4]p[a4]g[a4][i1][o0] ?F[a4]l[a4]nt[e3]\b/igu"
        ]
    },
]

def youtube(keywords):
    # Lista que irá armazenar as entradas geradas
    entries = []

    # Dicionário contendo os elementos do YouTube e seus respectivos comentários
    youtube_elements = {
        "Videos in related bar": [
            "#related ytd-compact-video-renderer",
        ],
        "Videos in general": [
            "ytd-video-renderer",
            "ytm-rich-item-renderer",
            "ytm-video-with-context-renderer",
            "ytm-media-item",
        ],
        "Videos in playlists": [
            "ytm-playlist-video-list-renderer",
            "ytm-media-item",
            "ytd-playlist-video-renderer",
            "ytm-media-item",
        ],
        "Channel": [
            "ytd-channel-renderer",
            "ytm-compact-channel-renderer",
        ],
        "Shorts": [
            "ytd-shelf-renderer",
            "ytd-reel-shelf-renderer",
            "ytd-rich-item-renderer",
            "ytm-reel-shelf-renderer",
            "ytm-shorts-lockup-view-model",
        ],
        "Playlists": [
            "ytm-compact-playlist-renderer",
        ]
    }

    custom_youtube_elements = {
        "Shorts": [
            "youtube.com##.ytGridShelfViewModelGridShelfItem:has(ytm-shorts-lockup-view-model:has-text(regex_keyword))"
        ]
    }

    # Itera sobre cada palavra-chave fornecida
    for keyword in keywords:
        # Itera sobre os elementos e comentários do dicionário
        for comment, element_list in youtube_elements.items():
            # Cria a entrada do AdBlock com base no elemento e na palavra-chave
            # A entrada é formatada para remover o conteúdo que contém a palavra-chave
            entries.append(f'! {comment}\n')
            for element in element_list:
                entries.append(f'youtube.com##{element}:has-text({keyword})\n')
        for comment, element_list in custom_youtube_elements.items():
            entries.append(f'! {comment}\n')
            for element in element_list:
                entries.append(f'{element.replace("regex_keyword", keyword)}\n')

    # Retorna a lista de entradas geradas
    return entries


def generate_for_all_files():
    for item in default_lists:
        path = os.path.join(os.getcwd(), item["default_path"])
        old_file = list_filter.load(path)
        entries = youtube(item["keywords"])
        old_file["entries"] = entries
        list_filter.save(old_file, path)
        list_filter.update_header(path)