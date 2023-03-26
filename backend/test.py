import unittest
from clase_ad import AD

class TestAD(unittest.TestCase):

    def setUp(self):
        self.ad = AD()

    def test_esta_user(self):
        self.assertTrue(self.ad.esta_user('pgarza'))
        self.assertFalse(self.ad.esta_user('not_a_username'))

    def test_buscar_rut(self):
        self.assertEqual(self.ad.buscar_rut('username'), '123456-7')
        self.assertEqual(self.ad.buscar_rut('not_a_username'), 'No se encuentra usuario')

    def test_cantidad_usuarios(self):
        self.assertEqual(self.ad.cantidad_usuarios(), 100)

    def test_extrae_rut_jefe(self):
        self.assertEqual(self.ad.extrae_rut_jefe('username'), '765432-1')
        self.assertEqual(self.ad.extrae_rut_jefe('not_a_username'), 'Usuario no posee jefe')

    def test_extraer_correo_jefatura(self):
        self.assertEqual(self.ad.extraer_correo_jefatura('username'), 'jefe@company.com')
        self.assertEqual(self.ad.extraer_correo_jefatura('not_a_username'), 'Usuario no posee jefe')

    def test_extraer_correo_manager(self):
        self.assertEqual(self.ad.extraer_correo_manager('username'), 'manager@company.com')
        self.assertEqual(self.ad.extraer_correo_manager('not_a_username'), 'Usuario no posee jefe')

    def test_obtener_empresa(self):
        self.assertEqual(self.ad.obtener_empresa('username'), 'Company')
        self.assertEqual(self.ad.obtener_empresa('not_a_username'), None)

    def test_hallar_ruts_repetidos(self):
        self.assertEqual(self.ad.hallar_ruts_repetidos(), ['123456-7', '987654-3'])

    def test_hallar_usernt_by_rut(self):
        self.assertEqual(self.ad.hallar_usernt_by_rut('123456-7'), 'username')
        self.assertEqual(self.ad.hallar_usernt_by_rut('not_a_rut'), 'No existe rut')

    def test_existe_usuario_by_rut(self):
        self.assertTrue(self.ad.existe_usuario_by_rut('123456-7'))
        self.assertFalse(self.ad.existe_usuario_by_rut('not_a_rut'))

    def test_nombre_by_usernt(self):
        self.assertEqual(self.ad.nombre_by_usernt('username'), 'User Name')

    def test_es_bl_bc_o_bd(self):
        self.assertTrue(self.ad.es_bl_bc_o_bd('bl20123'))
        self.assertFalse(self.ad.es_bl_bc_o_bd('username'))

    def test_fecha_de_creacion_desuso(self):
        self.assertGreaterEqual(self.ad.fecha_de_creacion_desuso('username'), 60)


    def test_integracion_usuarios_desuso_excel(self):
        import os
        usuarios_desuso = self.ad.usuarios_sin_logueo_pwdLastSet_o_lastLogonTimestamp_reciente()

        # Comprobar que la lista de usuarios desuso no esté vacía antes de generar el excel
        self.assertIsNotNone(usuarios_desuso)
        self.assertGreater(len(usuarios_desuso), 0)

        self.ad.generar_excel_desuso_completo()

        # Verificar si se generó el archivo de excel
        self.assertTrue(os.path.isfile('datos_desuso/usuarios_desuso.xlsx'))

        # Limpiar: eliminar el archivo generado para la prueba
        os.remove('datos_desuso/usuarios_desuso.xlsx')





