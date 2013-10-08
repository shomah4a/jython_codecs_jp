#-*- coding:utf-8 -*-


def main():

   print u'あいうえお'.encode('cp932')
   print u'あいうえお'.encode('cp932').decode('cp932').encode('utf-8')



if __name__ == '__main__':
    main()
