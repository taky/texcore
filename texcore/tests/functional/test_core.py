# -*- coding: utf-8 -*-
import xmlrpclib

from nose.tools import *

from texcore.tests import *
from texcore.tests.functional import XMLRPCControllerTestBase

class TestCoreController(XMLRPCControllerTestBase):
    def test_typeset(self):
        corps = r'''%
\documentclass{jsarticle}
\begin{document}
test!
\end{document}
'''
        pdf = self.xc.typeset(xmlrpclib.Binary(corps))
        assert 'PDF' in pdf.data

    @raises(xmlrpclib.Fault)
    def test_typeset__with_invalid_charset(self):
        corps = ur'''%
\documentclass{jsarticle}
\begin{document}
test!ふははははははあ
\end{document}
'''.encode('cp932')
        self.xc.typeset(xmlrpclib.Binary(corps))

    def test_typeset_with_param_1(self):
        corps = ur'''%
\documentclass{jsarticle}
\begin{document}
test!ふははははははあ
\end{document}
'''.encode('cp932')
        pdf = self.xc.typeset(xmlrpclib.Binary(corps), dict(encoding='cp932'))
        assert 'PDF' in pdf.data

    def test_typeset_with_param_2(self):
        corps = r'''%
\documentclass{jsarticle}
\begin{document}
test!
\end{document}
'''
        pdf = self.xc.typeset(xmlrpclib.Binary(corps), dict(papersize='a4'))
        assert 'PDF' in pdf.data

    def test_typeset_with_param_3(self):
        corps = ur'''%
\documentclass{jsarticle}
\begin{document}
test!ふははははははあ
\end{document}
'''.encode('cp932')
        pdf = self.xc.typeset(xmlrpclib.Binary(corps), dict(encoding='cp932', papersize='a4', embedmap=['ptex-kozuka', 'otf-kozuka']))
        assert 'PDF' in pdf.data

