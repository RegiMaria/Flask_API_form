| Recurso                                                      | Ação                                                         |
| :----------------------------------------------------------- | :----------------------------------------------------------- |
| **Register Endpoint [/register]**        Este endpoint permite que os usuários se registrem na aplicação. | **Registrar Usuário [POST]**                                                                                     **Request (application/json):**                                                                                Headers: Content-Type: application/json                                                                  Body: { "username": "string",      "email": "string"  }                                           **Response 200 (application/json)**:                                                                             Body {    "message": "Dados cadastrados com sucesso na API"  }                              **Response 400 (application/json):**                                                                             Body {      "error": "Dados inválidos"  }                                                              **Response 405 (application/json) :**                                                                              Body  {       "error": "Método não permitido"   } |

| Recurso                                                      | Ação                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **API Register [/api/register]**  Endpoint usado para registrar usuários na API. | **Registrar Usuário [POST]**                                                                                      **Request (application/x-www-form-urlencoded)**                                                  Body:  username (string, required): O nome de usuário do usuário                       email (string, required): O endereço de e-mail do usuário                                     **Response 200 (application/json): **                                                                                                Body  {  "message": "Dados cadastrados com sucesso na API"  }                                  **Response 400 (application/json):**                                                                         Body {      "error": "Dados inválidos"  }                                                                        **Response 405 (application/json):  **                                                                              Body {      "error": "Método não permitido"  } |



| Recurso                                                      | Ação                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Get Users [/api/usuarios]**  Endpoint é usado para obter a lista de usuários cadastrados na API. | **Obter Usuários [GET]**                                                                         **Response 200 (application/json):**                                                         Body                                                                                                                [      {          "username": "string",          "email": "string"      }  ] |





