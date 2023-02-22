from enum import Enum, auto
from typing import Tuple, List


class DialetoMiguxes(Enum):
    MIGUXES_ARCAICO = auto()
    MIGUXES_MODERNO = auto()
    NEO_MIGUXES = auto()

    __REGEX_GERAL = [
        (r'\buma?\b', '1'),
        (r'\b(dois | duas)\b', '2'),
        (r'\btrês\b', '3'),
        (r'\bquatro\b', '4'),
        (r'\bcinco\b', '5'),
        (r'\bseis\b', '6'),
        (r'\bsete\b', '7'),
        (r'\boito\b', '8'),
        (r'\bnove\b', '9'),
        (r'\bdez\b', '10'),
        (r'\bonze\b', '11'),
        (r'\bdoze\b', '12'),
        (r'\btreze\b', '13'),
        (r'\b(catorze|quatorze\b)', '14'),
        (r'\bquinze\b', '15'),
        (r'\bdezesseis\b', '16'),
        (r'\bdezessete\b', '17'),
        (r'\bdezoito\b', '18'),
        (r'\bdezenove\b', '19'),
        (r'\b([0-9]+) vez(es)?\b', r'\1x'),
        (r'\b(\d+) horas?\b', r'\1h'),
        (r'\b(\d+) minutos?\b', r'\1min'),
        (r'\bsegunda-feira\b', '2a'),
        (r'\bterça-feira\b', '3a'),
        (r'\bquarta-feira\b', '4a'),
        (r'\bquinta-feira\b', '5a'),
        (r'\bsexta-feira\b', '6a'),
        (r'\baté mais\b', 't+'),
        (r'\bdemais\b', 'd+'),
        (r'\bmais ou menos\b', '+-'),
        (r'\bmais\b', '+'),
        (r'\bmenos\b', '-'),
        (r'\bmei[ao]\b', '1/2'),
        (r'\bpor\s?qu[eê]', 'pq'),
        (r'\bhoje\b', 'hj'),
        (r'\btambém\b', 'tb'),
        (r'\bbeleza\b', 'blz'),
        (r'\bfirmeza\b', 'fmz'),
        (r'\bquando\b', 'qdo'),
        (r'\bquant([ao])(s?)\b', r'qt\1\2'),
        (r'\bmuit([ao])(s?)\b', r'mt\1\2'),
        (r'\bbeij(o|ão)\b', r'bj\1'),
        (r'\bbeijos\b', 'bjs'),
        (r'\btecl(e|ar|ou|amos)\b', 'tc'),
        (r'\binternet\b', 'net'),
        (r'\be-?mail(s?)\b', r'meio\1'),
        (r'\b(grana|dinheiro)\b', '$$$$$$'),
        (r'\best(ar|ou|ava|ive|aria|ão)\b', r't\1'),
        (r'\bestá([^\wáéíóúàâêôãõüç]|$)', r'tah\1'),
        (r'\bpara ([ao]s?)\b', r'pr\1'),
        (r'\bpara([^\wáéíóúàâêôãõüç-]|$)', r'pra\1'),
        (r'([aei]r)mos\b', r'\1'),
        (r'\bacab', 'cab'),
        (r'eix', 'ex'),
        (r'á([^\wáéíóúàâêôãõüç]|$)', r'ah\1'),
        (r'é([^\wáéíóúàâêôãõüç]|$)', r'eh\1'),
        (r'í([^\wáéíóúàâêôãõüç]|$)', r'ih\1'),
        (r'ó([^\wáéíóúàâêôãõüç]|$)', r'oh\1'),
        (r'ú([^\wáéíóúàâêôãõüç]|$)', r'uh\1'),
        (r'[áàâãä]', 'a'),
        (r'[éèêë]', 'e'),
        (r'[íìîï]', 'i'),
        (r'[óòôõö]', 'o'),
        (r'[úùûü]', 'u'),
    ]
    REGEX_MIGUXES_ARCAICO = [*__REGEX_GERAL,
                             (r'\b(\d+) segundos?\b', r'\1s'),
                             (r'\bprimeir([ao])\b', r'1\1'),
                             (r'\bsegund([ao])\b', r'2\1'),
                             (r'\bterceir([ao])\b', r'3\1'),
                             (r'\bquart([ao])\b', r'4\1'),
                             (r'\bquint([ao])\b', r'5\1'),
                             (r'\bsext([ao])\b', r'6\1'),
                             (r'\bsétim([ao])\b', r'7\1'),
                             (r'\boitav([ao])\b', r'8\1'),
                             (r'\bnon([ao])\b', r'9\1'),
                             (r'\bdécim([ao])\b', r'10\1'),
                             (r'\bfi(m|nal)de semana\b', 'fds'),
                             (r'\bcom([^\wáéíóúàâêôãõüç]|$)', r'c/\1'),
                             (r'\bque\b', 'q'),
                             (r'\b(você|voce)', 'vc'),
                             (r'\be-?mail(s?)\b', r'mail\1'),
                             (r'[ç]', 'c'),
                             (r'\b(he|ha|hi|ho|hua){2,}h?\b', 'rsrsrs'),
                             (r'!', '!!'),
                             (r'\?', '??')]
    REGEX_MIGUXES_MODERNO = [
        *__REGEX_GERAL,
        (r'\b(\d+) segundos?\b', r'\1s'),
        (r'\bprimeir([ao])\b', r'1\1'),
        (r'\bsegund([ao])\b', r'2\1'),
        (r'\bterceir([ao])\b', r'3\1'),
        (r'\bquart([ao])\b', r'4\1'),
        (r'\bquint([ao])\b', r'5\1'),
        (r'\bsext([ao])\b', r'6\1'),
        (r'\bsétim([ao])\b', r'7\1'),
        (r'\boitav([ao])\b', r'8\1'),
        (r'\bnon([ao])\b', r'9\1'),
        (r'\bdécim([ao])\b', r'10\1'),
        (r'\bfi(m|nal) de semana\b', 'fds'),
        (r'\bmesm[ao](s?)\b', r'msm\1'),
        (r'\bdepois\b', 'dpois'),
        (r'\bquem\b', 'qm'),
        (r'\bcomigo\b', 'cmg'),
        (r'\bcadê|cade', 'kd'),
        (r'\bqualquer\b', 'qq'),
        (r'\bfalou\b', 'flw'),
        (r'\bvaleu\b', 'vlw'),
        (r'\btchau\b', 'xau'),
        (r'\bque\b', 'ke'),
        (r'\bvocês\b', '6'),
        (r'\bvocê|voce', 'vc'),
        (r'\badicion', 'adde'),
        (r'\bamig([ao]|ão)\b', r'mig\1'),
        (r'\blind([ao]|ão|ona)\b', r'leend\1'),
        (r'\bnovidade(s?)\b', r'9dad\1'),
        (r'\bpr[ao]([^áéíóúàâêôãõüç]|$)', r'p\1'),
        (r'ão\b', 'aum'),
        (r'([aei])ndo\b', r'\1no'),
        (r'([crt]ad)([ao])\b', r'\1eenh\2'),
        (r'foto(s?)\b', 'foteenha$1'),
        (r'(\w)tinh([ao])\b', r'\1teenh\2'),
        (r'\bse\b', 'c'),
        (r'\bde\b', 'd'),
        (r'\bte\b', 't'),
        (r'ch', 'x'),
        (r'sh', 'x'),
        (r'qu', 'k'),
        (r'(\w(ss|[cdgtv]))e(s?)m?\b', r'\1i\3'),
        (r'\bseg', 'sig'),
        (r'\bdes([^s])', r'dis\1'),
        (r'\bbonit', 'bunit'),
        (r'\be\b', 'i'),
        (r'[ç]', 'ss'),
        (r'(\w[a-z])l\b', r'\1u'),
        (r'o(s?)\b', r'u\1'),
        (r'\b(\d+)u\b', r'\1o'),
        (r'(\w)ou\b', r'\1o'),
        (r'\bou(\w)', r'o\1'),
        (r'(\w)ou(\w)', r'\1o\2'),
        (r'\bc([^ei\W])', r'k\1'),
        (r'ar\b', 'ah'),
        (r'er\b', 'e'),
        (r'ir\b', 'i'),
        (r'eira\b', 'era'),
        (r'([^s\W])sa\b', r'\1za'),
        (r'\b(he|ha|hi|ho|hua|rs){2,}h?\b', 'huahuahua'),
        (r'[8:][-o]?[D)]', 'huahuahua'),
        (r'\.', '......'),
        (r'\,', '...'),
        (r'\, (\n|$)', r'...\1'),
        (r'!', '!!!!!'),
        (r'\?', '??!?!'),
    ]
    REGEX_NEO_MIGUXES = [
        *__REGEX_GERAL,
        (r'\bcom([^\wáéíóúàâêôãõüç]|$)', r'cum\1'),
        (r'\bmesm[ao](s?)\b', r'msm\1'),
        (r'\bdepois\b', 'dpois'),
        (r'\bquem\b', 'qm'),
        (r'\bcomigo\b', 'cmg'),
        (r'\bcadê', 'kd'),
        (r'\bqualquer\b', 'qq'),
        (r'\bfalou\b', 'flw'),
        (r'\bvaleu\b', 'vlw'),
        (r'\btchau\b', 'xau'),
        (r'\bque\b', 'ki'),
        (r'\b(adoro você|te adoro)', 'adoluxê'),
        (r'\bamo vocês\b', 'amodolu vocês'),
        (r'\b(amo você|te amo)', 'te amodolu'),
        (r'\b(você|voce)', 'vuxê'),
        (r'\badicion[\wáí]+', 'add'),
        (r'\bamig([ao]s?)\b', r'migux\1'),
        (r'\blind([ao]s?)\b', r'lindux\1'),
        (r'\bfof([ao]s?)\b', r'fofux\1'),
        (r'\bdormir\b', 'mimir'),
        (r'\bnome(s?)\b', r'nominho\1'),
        (r'\besposa\b', 'marida'),
        (r'\b(de novo|novamente)\b', 'dinovo'),
        (r'\b(aliás|por exemplo|digamos que)\b', 'tipo assim'),
        (r'ão\b', 'aum'),
        (r'(\w[aei])ndo\b', r'\1no'),
        (r'(\w[crt]ad)([ao])\b', r'\1eenh\2'),
        (r'foto(s?)\b', r'foteenha\1'),
        (r'(\w)tinh([ao])\b', r'\1teenh\2'),
        (r'\bse\b', 'si'),
        (r'\bde\b', 'di'),
        (r'\bte\b', 'ti'),
        (r'ch', 'x'),
        (r'sh', 'x'),
        (r'qu', 'k'),
        (r'(\w(ss|[cdgtv]))e(s?)m?\b', r'\1i\3'),
        (r'\bseg', 'sig'),
        (r'\bdes([^s])', r'dis\1'),
        (r'\bbonit', 'bunit'),
        (r'\be\b', 'i'),
        (r'ês\b', 'eix'),
        (r'(\w)(ás|az)\b', r'\1aix'),
        (r'[ç]', 'ss'),
        (r'(\w[a-z])l\b', r'\1u'),
        (r'o(s?)\b', r'u\1'),
        (r'\b(\d +)u\b', r'\1o'),
        (r'(\w)ou\b', r'\1ow'),
        (r'\bou(\w)', r'o\1'),
        (r'(\w)ou(\w)', r'\1o\2'),
        (r'\bc([^ei\W])', r'k\1'),
        (r'ar\b', 'ah'),
        (r'er\b', 'e'),
        (r'ir\b', 'i'),
        (r'eira\b', 'era'),
        (r'([^s\W])sa\b', r'\1za'),
        (r'([^\Ws])s\b', r'\1x'),
        (r'(\w)a\b', r'\1ah'),
        (r'\b(he|ha|hi|ho|hua|rs){2,}h?\b', 'kkkkkkkkkkk'),
        (r'[8:][-o]?[D)]', 'kkkkkkkkkkk'),
        (r'\.', '......'),
        (r'\,', '...'),
        (r'\, (\n|$)', r'...\1'),
        (r'!', '!!!!!'),
        (r'\?', '??!?!'),
        (r'[éèêë]', 'e'),
    ]

    @classmethod
    def pegar_regex_por_dialeto(cls, dialeto: 'DialetoMiguxes') -> List[Tuple[str, str]]:

        """
        Seleciona a lista de RegEx relativa ao dialeto de miguxês

        Parameters
        ----------
        dialeto: DialetoMiguxes
            Um dialeto de miguxês
        
        Returns
        -------
        regex: List[Tuple[str, str]]

        """

        if dialeto == DialetoMiguxes.NEO_MIGUXES:
            return cls.REGEX_NEO_MIGUXES.value
        elif dialeto == DialetoMiguxes.MIGUXES_ARCAICO:
            return cls.REGEX_MIGUXES_ARCAICO.value
        else:
            return cls.REGEX_MIGUXES_MODERNO.value
