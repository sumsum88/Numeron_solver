## Description
ヌメロン(numeron)という数当てゲームをコマンドラインで遊べるものです.
CPUは情報エントロピーH(次の一手|今までに得た情報)を最大化するように次の一手を選択します.
(ただ計算量の関係で情報量の計算を簡略化しているので最適かどうかはわからないです)

## Requirement
python 2.7 ,
numpy

## Usage
python main.pyでコンピュータとnumeronの対戦ができます.
(playerのクラスを変えることでコンピュータ同士、人間同士の対戦も可能です)

common.pyのCHARS(文字の種類)とDIGITS(桁数)を変える事で様々な条件での対戦が可能です、ただしCHARSを長くしすぎないことを推奨します.

## Author
[sumsum88](https://github.com/sumsum88)