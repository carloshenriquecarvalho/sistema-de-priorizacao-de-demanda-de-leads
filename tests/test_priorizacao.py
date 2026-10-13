import unittest
import src.domain.priorizacao as priorizacao
from unittest.mock import patch

class TestPriorizacao(unittest.TestCase):
    @patch("builtins.input", return_value="nao")
    def test_vendedor_tem_leads_novo_contato_nao_elegivel(self, mock_input):
        resultado = priorizacao.verifica_criterio_etapa_novo_lead_vazia()

        self.assertFalse(resultado)
        mock_input.assert_called_once()

    @patch("builtins.input", return_value="sim")
    def test_vendedor_nao_tem_leads_novo_contato_elegivel(self, mock_input):
        resultado = priorizacao.verifica_criterio_etapa_novo_lead_vazia()

        self.assertTrue(resultado)
        mock_input.assert_called_once()

    

if __name__ == '__main__':
    unittest.main(verbosity=2)