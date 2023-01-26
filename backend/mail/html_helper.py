from string import Template

#Template html
html ='''\
<html>
	<head>
		<title></title>
	</head>
	<body>
		<table role="presentation" style="width: 100%; border-collapse: collapse; border: 0; border-spacing: 0; background: #ffffff;">
			<tbody>
				<tr>
					<td align="center" style="padding: 0;">
						<table role="presentation" style="width: 601px; border-collapse: collapse; border: 1px solid #cccccc; border-spacing: 0px; text-align: left;">
							<tbody>
								<tr>
									<td align="center" style="padding: 40px 0px 30px; background: #f3f3f3; width: 599.006px;">
										<img alt="WSO Worldwide Security Options – ¡Su decisión inteligente!" class="n3VNCb" data-noaft="1" height="150" src="$logo" width="162" /></td>
								</tr>
								<tr>
									<td style="padding: 36px 30px 42px; width: 539.006px;">
										<table role="presentation" style="width: 100%; border-collapse: collapse; border: 0; border-spacing: 0;">
											<tbody>
												<tr>
													<td style="padding: 0 0 36px 0; color: #153642;">
														<h1 style="font-size: 24px; margin: 0 0 20px 0; font-family: Arial,sans-serif;">
															Reporte de Cuentas en Desuso</h1>
														<p style="margin: 0 0 12px 0; font-size: 16px; line-height: 24px; font-family: Arial,sans-serif;">
															Se adjunta reporte de la fecha $fecha el cual muestra el total de usuarios en desuso de la empresa $empresa</p>
													</td>
												</tr>
												<tr>
													<td style="padding: 0;">
														&nbsp;</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
								<tr>
									<td style="padding: 30px; background: #2b0e62; width: 539.006px;">
										<table role="presentation" style="width: 100%; border-collapse: collapse; border: 0; border-spacing: 0; font-size: 9px; font-family: Arial,sans-serif;">
											<tbody>
												<tr>
													<td align="left" style="padding: 0; width: 50%;">
														<p style="margin: 0; font-size: 14px; line-height: 16px; font-family: Arial,sans-serif; color: #ffffff;">
															&reg; Grupo Security</p>
													</td>
													<td align="right" style="padding: 0; width: 50%;">
														<table role="presentation" style="border-collapse: collapse; border: 0px; border-spacing: 0px; height: 37px;">
															<tbody>
																<tr style="height: 38px;">
																	<td style="padding: 0px 0px 0px 10px; width: 38px; height: 37px;">
																		&nbsp;</td>
																	<td style="padding: 0px 0px 0px 10px; width: 38px; height: 37px;color:">
																		&nbsp;</td>
																</tr>
															</tbody>
														</table>
													</td>
												</tr>
											</tbody>
										</table>
									</td>
								</tr>
							</tbody>
						</table>
					</td>
				</tr>
			</tbody>
		</table>
		<p>
			&nbsp;</p>
	</body>
</html>
'''


def reporte_html(fecha:str,empresa:str,logo:str):

    """Funcion que parsea el html y retorna un html reemplazando las variables por los valores recibidos"""
    s = Template(html).safe_substitute(fecha=fecha,empresa=empresa,logo=logo)

    return s

