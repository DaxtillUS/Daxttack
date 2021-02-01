import os
import time
import sys

print (''' \033[31m

MMMMMMMMMMMMMMMMMMMMMMMMMMMMMmmhhyyshyysyyhhhhhyyysyyyoyyhhmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMNmhyssyyhhhhhhyssooooooossyyhhddhhyyssyhmMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNhyyyhhhhys+/:::/++oossssssoo+//:::/oshhhhhyysyNMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMmysyhdhhs/::/oshhhhhhhysohhdhhh+oyhhhhys+:::+yhhhhyoymMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMNhsshhhy+::+yhhhhdhy+/:ss  /ddddds-` `.:+ohhhhho/-:ohhhhsshNMMMMMMMMMMMMMMM
MMMMMMMMMMMMMmssyhhy+-/shhhdhhddddho-  ` .hddddddhs  ./--hddhhshhy+::ohhhyssmMMMMMMMMMMMMM
MMMMMMMMMMMmyshhho::shhh+.:oyhhhhhhhhs    :shhhhhh-  shhdhhhh: `ohhhy+-/yhhhosmMMMMMMMMMMM
MMMMMMMMMmsohhho-/yhhdh:  .` `:+shhhh- .o-  -yhhh+  /hhhhhhh-  +hhhhhyhs::yhhhosmMMMMMMMMM
MMMMMMMMhshhho-+hddhhhhh. -s- ` .shho`-ohhyhhhhhhyo/hhhhhhy. `ohhhhs. :hhs::yhhyohMMMMMMMM
MMMMMMmoshhy-:yhdhhhhhhhy.  `+hyhhhdhdhhdhhhhhhhhhhhhhhhhh/``shhhs-  -shhhho.+hhhsomMMMMMM
MMMMMhoydh+.shdhhysyhhhhhy` :hhhhhhys+:-.``     `.-:/oyhhhhhhhhy:  .shhhhhhhh/-yhhy+hMMMMM
MMMMd+hhh::hhhh+.   `:shhhyohhhho:.                    `:+yhhhs`  -hhhhhhhhdhho.ohhh/hMMMM
MMMh+hhy-/hhhy- -sy+. `shhhhho-         .-+sssyo/-         -ohhh/` .+hhhhhhhyhhy.+hhh+dMMM
MMhohhy.+hhhh:` `:oho `shhh+`       `/yNMMMMMMMMMMNy-        `/hhh+.:yhhhs/. .yhy.+hhh+hMM
Mdshhh-/hhhhhhho-  ``.shh+`       :yNMMMMMMMMMMMMMMMMdo`       `+hhhhh+-`  ./shhhy.ohhh+dM
Nsyhh/-hhhhhhhhhhy+.:hhy-       /mMMMMMMMMMMMMMMMMMMMMN.         -yhhy.  +yhhhhhhhs`yhhsoN
hohhs`ydhhhhhhhhhhhhhhs.        sMMMMMMMMMMMMMMMMMMMMMd           .yhhh: .yhhhhhhhh/-hhh+h
ohhh-/hdhhhhhhhhhhhdhy`         .NMMMMMMMMMMMMMMMMMMMMy            .yhdh/`/hhhhhhhhh`ohhyo
ohhs`hhhhhhhhhhhhhhhh.           oMMMMMMMMMMMMMMMMMMMM+             -hhhhhhhhhhhhhhh+-hhh+
shd/:dhhhhhhhhhhhhdh+            `dMMMMNdyooo+++sdMMMN.              ohhhhhhhhhhhhhhy`yhho
hhh.+hhhhhhhhhhhhhhh.             -NMMN++sh- :hyo--hMs               -dhhhhhhhhhhhhdh.ohhy
hdh`shhhhhhh+/ohhhhy               /m+.+//+- ./.:- `do               `hhhhhho+shhhhdh:/dhh
dhh`yhdhhhh:   ohhhy               -+:              ..               `hhhhh:   shhhhh:/hhh
hhh`shdhhhhh+/ohhhhy                -hh.  :hy/-     .                `hhhhhy/:+hhhhhh:/ddh
hhh.ohhhhhhhhhhhhhhh.                :Nm`/ss+yo-   `.                :dhhhhhhhhhhhhdh.ohhh
yhh/:dhhhhhhhhhhhhhh+                 om/-.os.``-/s                  shhhhhhhhhhhhhhy`yhds
shhs`hhhhhhhhhhhhhhhh.                 hMs-..``:s-`                 :hhhhhhhhhhhhhhh+-hhho
yhhh-+dhhhhhhhhhhhhhhy`               `.+hMMds/.  /h.              -hddhhhhhhhhhhhhh.ohhhs
dyhhs`yhhdhhhhhhhhhhhhs`             /Ns``+o`  .ohMMNs`           -hhhhhhhhhhhhhhhh/.hhhsd
Nyhhh:-hhdhhhhhhhhhhhhhy-        `-+dMNym+::/smmmMMMMMNy/.      `/hhhhy+//ohhhhhhhs`yhhhyN
MNyhhh./hdhhhhhhhh+:shhhh+`  ./ymNMMMMN`-yNh+.`.dMMMMMMMMMmho:`-shdhy- .-:osyhhhhy.+hhhsmM
MMdyhhy.+hhhhhhhs.   ./yhhh+/dMMMMMMMMN`-dh`  :mMMMMMMMMMMMMNNmdhhhh. `/-`   -hhy./hhhydMM
MMMdyhhy./hhhhh/   -s+. /hdhhdNMMMMMMMM/mNmo`sMMMMMMMMMMMMmdddhhhhhh+` `./o. `yy.+hhhsdMMM
MMMMmhhhh::hhh-  :o- -yshhhhhhdhhdNMMMMomNNydMMMMMMMMNmddddhhhhhhhhhhhy/..``:yo.ohhhymMMMM
MMMMMmdhhh+.shho- .+sshhhhhhhhhhdhdddhhsydsmmmdddmmmdhhhhhys+yhhhhhhhhhs//ohh/-yhhhhdMMMMM
MMMMMMNdhhhy-:yhhy/`+hhhhhhhhhhhhhhhoosyhhddhhhhhhhhyo/yhh+  :hhhhhhhhhhhhhs.+hhhhhNMMMMMM
MMMMMMMMNddhho-+hhhhhhhhhhhhhhhhhhh:   `yhhhhhhhhhhh+  -hhh.  ohhhhhhhdhhy::yhhhhmMMMMMMMM
MMMMMMMMMMmdhhh+-+yhhhddddddddhhhy. .+  ohhhhhhhhhhhh-  ohhs  .hdddhhhhs::shhhhdNMMMMMMMMM
MMMMMMMMMMMMmdhhho-:shhdddddddhho`  /+  :hhhhhhhhhhhhs` `+o:  /hdhhhy+-/yhdhhmMMMMMMMMMMMM
MMMMMMMMMMMMMMddhhhy/-/shhdddhho.`-/:-  .hdddddddddddhy:...:+yhhhy+::ohhhhddMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMNmddhhy+-:+yhhhhhhhddh+:-yddhddddddddddddhdhhhs/-:ohhhhddNMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNmdhhhhs/::/oyhhhhhhhdhhhhhhdhhdhhhhhys+:::+yhhhhdmNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNmddhhhhyo+::::/+oosssssssoo+//:::/+shhhhhddmNMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNNmdddhhhdhhhyssoooooooosyyhhhhhhhdddmNMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNmmmddddddhhhhhhhhhdddddmmmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
   ======================================================================================
                          :D:E:V:E:L:O:P:E:D: :B:Y: :D:A:X:T:I:L:L:
   ======================================================================================

           NOT:İLLEGAL OLARAK KULLANILMASI BENİM SORUMLULUĞUMDA DEĞİLDİR\033[0m''')

    
time.sleep(2)
