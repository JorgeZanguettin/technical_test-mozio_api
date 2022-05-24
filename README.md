# Django Project

# Routes

### GET /api/providers/
`Get all providers`


### POST /api/providers/
`Insert a new provider`

### GET /api/provider/<int:id>/
`Get detail of a provider`

### GET /api/providers/<int:id>/polygons/
`Get all polygons of a provider`

### PUT /api/provider/<int:id>/
`Modify a exists provider`

### DELETE /api/provider/<int:id>/
`Delete a exists provider`

<br><br>

### GET /api/polygons/
`Get all polygons`

### POST /api/polygons/
`Insert a new polygon`

### GET /api/polygon/<int:id>/
`Get detail of a polygon`

### PUT /api/polygon/<int:id>/
`Modify a exists polygon`

### DELETE /api/providers/<int:id>/
`Delete a exists polygon`

<br><br>

### GET /api/polygons/<str:coord>/
`Get all polygons in a coordenates`