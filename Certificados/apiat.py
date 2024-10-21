import requests


class Certificados():

    def __init__(self) -> None:
        self.url = "https://reepre.service-now.com/api/now/table/u_cmdb_ci_certificate"
        self.user = 'UG_AUTOMATINT_RPA'
        self.pwd = 'aUto+2020'
        self.headers = {"Content-Type":"application/json","Accept":"application/json"}

    def getCertificado(self, finger):
        """Función para consultar si el certificado existe

        Returns:
            data: .json de salida de la ejecución con los valores de los campos del certificado

        Raises:
            er: Error a la hora de establecer la conexión con la API
        """
        path_consulta = f'{self.url}?sysparm_query=u_fingerprintLIKE{finger}&sysparm_limit=1'

        try:
            response = requests.get(path_consulta, auth=(self.user, self.pwd), headers=self.headers )

            if response.status_code != 200:
                # self.log.warning(f"Resultado de la llamada a la API \n {response}")
                raise Exception("No se ha podido establecer la conexión con la API")
            else:
                # self.log.info("Se ha establecido la conesión con la API")
                print("Se ha establecido conexión con la API")

            data = response.json()

            return data

        except Exception as er:
            # self.log.error(f"Ha habido un problema a la hora de establecer la conexión con la API:{er}")
            raise er

    # def putCertificado(self, sys_id):
    #     """Función para realizar el put del certificado



    #     Returns:
    #         data: .json de salida de la ejecución con los valores de los campos del certificado

    #     Raises:
    #         er: Error a la hora de establecer la conexión con la API
    #     """
    #     path_post = f'{self.url}/{sys_id}'
    #     # u_fingerprint = "ED:F4:18:47:89:0C:12:7F:23:6B:42:81:00:0E:A2:6C:59:58:CB:BC"

    #     # data = f'{{"u_fingerprint":"{u_fingerprint}"}}'

    #     try:
    #         response = requests.put(path_post, auth=(self.user, self.pwd), headers=self.headers ,data="{\"u_fingerprint\":\"ED:F4:18:47:89:0C:12:7F:23:6B:42:81:00:0E:A2:6C:59:58:CB:BC\"}")

    #         if response.status_code != 200:
    #             # self.log.warning(f"Resultado de la llamada a la API \n {response}")
    #             raise Exception("No se ha podido establecer la conexión con la API")
    #         else:
    #             # self.log.info("Se ha establecido la conesión con la API")
    #             print("Se ha establecido conexión con la API")

    #         # Decode the JSON response into a dictionary and use the data
    #         data = response.json()

    #         return data

    #     except Exception as er:
    #         # self.log.error(f"Ha habido un problema a la hora de establecer la conexión con la API:{er}")
    #         raise er

def main():
    """Función main

    Raises:

    """

# try:

    u_fingerprint = 'ED:F4:18:47:89:0C:12:7F:23:6B:42:81:00:0E:A2:6C:59:58:CB:BC'

    certificados = Certificados()

    getresp = certificados.getCertificado(u_fingerprint)

    if 'result' not in getresp or getresp["result"] is None or not getresp['result']:
        print("No se ha encontrado el certificado, se porcede a hacer el POST")
    else:
        print("Se ha encontrado el certificado se procede a realizar el PUT")

        sys_id = getresp['result'][0]['sys_id']

        putresp = certificados.putCertificado(sys_id)

        print(f"El put se ha realizado correctamente. El certificado tiene los valores: \n {putresp}")


if __name__ == '__main__':

    main()