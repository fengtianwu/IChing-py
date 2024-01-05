#!/usr/bin/env python
import numpy as np
import datetime
import hashlib
import re

hexagram64=[
    "䷁ : 坤 (kūn)",
    "䷗ : 復 (fù)",
    "䷆ : 師 (shī)",
    "䷒ : 臨 (lín)",
    "䷎ : 謙 (qiān)",
    "䷣ : 明夷 (míng yí)",
    "䷭ : 升 (shēng)",
    "䷊ : 泰 (tài)",
    "䷏ : 豫 (yù)",
    "䷲ : 震 (zhèn)",
    "䷧ : 解 (xiè)",
    "䷵ : 歸妹 (guī mèi)",
    "䷽ : 小過 (xiǎo guò)",
    "䷶ : 豐 (fēng)",
    "䷟ : 恆 (héng)",
    "䷡ : 大壯 (dà zhuàng)",
    "䷇ : 比 (bǐ)",
    "䷂ : 屯 (zhūn)",
    "䷜ : 坎 (kǎn)",
    "䷻ : 節 (jié)",
    "䷦ : 蹇 (jiǎn)",
    "䷾ : 既濟 (jì jì)",
    "䷯ : 井 (jǐng)",
    "䷄ : 需 (xū)",
    "䷬ : 萃 (cuì)",
    "䷐ : 隨 (suí)",
    "䷮ : 困 (kùn)",
    "䷹ : 兌 (duì)",
    "䷞ : 咸 (xián)",
    "䷰ : 革 (gé)",
    "䷛ : 大過 (dà guò)",
    "䷪ : 夬 (guài)", 
    "䷖ : 剝 (bō)",
    "䷚ : 頤 (yí)",
    "䷃ : 蒙 (méng)",
    "䷨ : 損 (sǔn)",
    "䷳ : 艮 (gèn)",
    "䷕ : 賁 (bì)",
    "䷑ : 蠱 (gŭ)",
    "䷙ : 大畜 (dà xù)",
    "䷢ : 晉 (jìn)",
    "䷔ : 噬嗑 (shì kè)",
    "䷿ : 未濟 (wèi jì)",
    "䷥ : 睽 (kuí)",
    "䷷ : 旅 (lǚ)",
    "䷝ : 離 (lí)",
    "䷱ : 鼎 (tǐng)",
    "䷍ : 大有 (dà yǒu)",
    "䷓ : 觀 (guān)",
    "䷩ : 益 (yì)",
    "䷺ : 渙 (huàn)",
    "䷼ : 中孚 (zhōng fú)",
    "䷴ : 漸 (jiàn)",
    "䷤ : 家人 (jiā rén)",
    "䷸ : 巽 (xùn)",
    "䷈ : 小畜 (xiǎo xù)",
    "䷋ : 否 (pǐ)",
    "䷘ : 無妄 (wú wàng)",
    "䷅ : 訟 (sòng)",
    "䷉ : 履 (lǚ)",
    "䷠ : 遯 (dùn)",
    "䷌ : 同人 (tóng rén)",
    "䷫ : 姤 (gòu)",
    "䷀ : 乾 (qián)"
    ]

#input info
########################################################
owner  =input("Owner:")
about  =input("About:")
now    =datetime.datetime.now()

info  ="{:>8} : {}\n{:>8} : {}\n{:>8} : {}\n".format("Owner", owner ,"About", about, "Date", now)
########################################################
digest =hashlib.md5(info.encode('utf-8')).hexdigest()
rng    =np.random.default_rng(int(digest,16))

original = rng.integers(8, size=6)    
########################################################

lines = np.array(['1','0','0','1','0','1','1','0'])[original].tolist()
alter = np.array(['.',' ',' ',' ',' ',' ',' ','.'])[original].tolist()

hexagram=hexagram64[int(''.join(lines), 2)]
hexagram_symbol=re.split(':|\(|\)', hexagram)[0].strip(' ')
hexagram_name=re.split(':|\(|\)', hexagram)[1].strip(' ')
hexagram_pinyin=re.split(':|\(|\)', hexagram)[2].strip(' ')

########################################################

with open("{}".format(now), 'w') as f:
    f.write(64*'*' + '\n')
    f.write('{}'.format(info))
    f.write(64*'*' + '\n')
    f.write('{:>8} : {}\n'.format(''.join(list(map(str, original))), hexagram_pinyin))
    f.write('{:>8} : {}\n'.format(''.join(alter),hexagram_name))
    f.write('{:>8} : {}\n'.format(''.join(lines),hexagram_symbol))
    f.write(64*'*' + '\n')
    f.write("https://zh.wikisource.org/wiki/周易/{}\n\n".format(hexagram_name))
 
