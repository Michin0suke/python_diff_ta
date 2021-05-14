import os
import difflib
import base64

tree = [
  # 1
    [
      {
        'type': 'file',
        'name': 'hellow.py',
        'content': b'IyBoZWxsb3cucHk6IOacgOWIneOBrkZsYXNr44Ki44OX44OqCmZyb20gZmxhc2sgaW1wb3J0IEZsYXNrCmZyb20gZmxhc2sgaW1wb3J0IHJlbmRlcl90ZW1wbGF0ZSAjIOi/veWKoApmcm9tIGZsYXNrIGltcG9ydCByZXF1ZXN0ICMg6L+95YqgCgphcHAgPSBGbGFzayhfX25hbWVfXykKCiMg44OI44OD44OXCkBhcHAucm91dGUoJy8nKQpkZWYgaGVsbG93X3dvcmxkKCk6CiAgICBtb2ppcmV0c3UgPSAn44KI44GG44GT44Gd44CBRmxhc2vjga7kuJbnlYzjgbjvvIEnCiAgICAjcHJpbnQobW9qaXJldHN1KQogICAgI3JldHVybiBtb2ppcmV0c3UKICAgIHJldHVybiByZW5kZXJfdGVtcGxhdGUoJ2luZGV4Lmh0bWwnLCBteXN0ciA9IG1vamlyZXRzdSkgIyDov73liqAK',
      },
      {
        'type': 'directory',
        'name': 'templates',
        'files': [
          {
            'type': 'file',
            'name': 'index.html',
            'content': b'eyMgaW5kZXguaHRtbCAjfQp7JSBleHRlbmRzICd0ZW1wbGF0ZS5odG1sJyAlfQp7JSBibG9jayBtYWluX2NvbnRlbnQgJX0KPCEtLSDmloflrZfliJfjgpLmjL/lhaUgLS0+Cnt7bXlzdHJ9fQp7JSBlbmRibG9jayAlfQ==',
          },
          {
            'type': 'file',
            'name': 'template.html',
            'content': b'PCFET0NUWVBFIGh0bWw+CjxodG1sPgogICAgPGhlYWRlcj4KICAgICAgICA8bWV0YSBjaGFyc2V0PSJVVEYtOCIgLz4KICAgICAgICA8dGl0bGU+Rmlyc3QgRmxhc2sgQXBwbGljYXRpb24gYnkgLS0tPC90aXRsZT4KICAgIDxib2R5PgogICAgICAgIDxoMT7mnIDliJ3jga5GbGFza+OCouODl+ODquOCseODvOOCt+ODp+ODszwvaDE+CiAgICAgICAgPGgyPi0tLTwvaDI+CiAgICAgICAgPGhyIC8+CiAgICAgICAgeyUgYmxvY2sgbWFpbl9jb250ZW50ICV9CiAgICAgICAgeyUgZW5kYmxvY2sgJX0KICAgICAgICA8aHIgLz4KICAgICAgICA8YWRkcmVzcz5Db3B5cmlnaHQgKGMpIDIwMjEgLS0tPC9hZGRyZXNzPgogICAgPC9ib2R5Pgo8L2h0bWw+',
          },
        ],
      },
    ],


    # 2
    [
      {
        'type': 'file',
        'name': 'input.py',
        'content': b'IyBpbnB1dC5weTog44OV44Kp44O844Og5YWl5Yqb44Gu5Ye65YqbCmZyb20gZmxhc2sgaW1wb3J0IEZsYXNrCmZyb20gZmxhc2sgaW1wb3J0IHJlbmRlcl90ZW1wbGF0ZQpmcm9tIGZsYXNrIGltcG9ydCByZXF1ZXN0CgphcHAgPSBGbGFzayhfX25hbWVfXykKCiMg44OI44OD44OXCkBhcHAucm91dGUoJy8nLCBtZXRob2RzID0gWydHRVQnLCAnUE9TVCddKSAjIFBPU1Tjga7jgb/lhaXlipvjgasKZGVmIHNob3dfaW5wdXQoKToKICAgIGlucHV0ID0gJ+WFpeWKm+OBquOBlycKICAgIGlmIHJlcXVlc3QubWV0aG9kID09ICdQT1NUJzoKICAgICAgICBpbnB1dCA9IHJlcXVlc3QuZm9ybVsnZm9ybV9pbnB1dCddICMgPGlucHV0IG5hbWU9ImZvcm1faW5wdXQiIC4uLj4KCiAgICByZXR1cm4gcmVuZGVyX3RlbXBsYXRlKCdpbmRleC5odG1sJywgbXlzdHIgPSBpbnB1dCk=',
      },
      {
        'type': 'directory',
        'name': 'templates',
        'files': [
          {
            'type': 'file',
            'name': 'index.html',
            'content': b'eyMgaW5kZXguaHRtbCAjfQp7JSBleHRlbmRzICd0ZW1wbGF0ZS5odG1sJyAlfQp7JSBibG9jayBtYWluX2NvbnRlbnQgJX0KPGZvcm0gbWV0aG9kPSJQT1NUIj4KICAgIDxwPuWFpeWKm+aWh+Wtl+WIlzogPGlucHV0IHR5cGU9InRleHQiIG5hbWU9ImZvcm1faW5wdXQiIHNpemU9IjMwIiAvPjwvcD4KICAgIDxwPgogICAgICAgIDxpbnB1dCB0eXBlPSJzdWJtaXQiIHZhbHVlPSLlhaXlipvnorrlrpoiIC8+CiAgICAgICAgPGlucHV0IHR5cGU9InJlc2V0IiB2YWx1ZT0i5raI5Y67IiAvPgogICAgPC9wPgo8L2Zvcm0+CjwhLS0g5YWl5Yqb44GM44GC44KM44Gw5paH5a2X5YiX44KS5oy/5YWlLS0+CjxwPuWFpeWKm+aWh+Wtl+WIlzogIHt7bXlzdHJ9fTwvcD4KeyUgZW5kYmxvY2sgJX0=',
          },
          {
            'type': 'file',
            'name': 'template.html',
            'content': b'PCFET0NUWVBFIGh0bWw+CjxodG1sPgogICAgPGhlYWRlcj4KICAgICAgICA8bWV0YSBjaGFyc2V0PSJVVEYtOCIgLz4KICAgICAgICA8dGl0bGU+IFNlY29uZCBGbGFzayBBcHBsaWNhdGlvbiBieSAtLS08L3RpdGxlPgogICAgPGJvZHk+CiAgICAgICAgPGgxPuODleOCqeODvOODoOOBruWFpeWKm+OBruWHuuWKmzwvaDE+CiAgICAgICAgPGgyPi0tLTwvaDI+CiAgICAgICAgPGhyLz4KICAgICAgICB7JSBibG9jayBtYWluX2NvbnRlbnQgJX0KICAgICAgICB7JSBlbmRibG9jayAlfQogICAgICAgIDxociAvPgogICAgICAgIDxhZGRyZXNzPkNvcHlyaWdodCAoYykgMjAyMSAtLS08L2FkZHJlc3M+CiAgICA8L2JvZHk+CjwvaHRtbD4=',
          },
        ],
      },
    ],

    # 3
    [
      {
        'type': 'file',
        'name': 'address.py',
        'content': b'IyBhZGRyZXNzLnB5OiDkvY/miYDpjLLjgqLjg5fjg6oKZnJvbSBmbGFzayBpbXBvcnQgRmxhc2ssIHJlbmRlcl90ZW1wbGF0ZSwgcmVxdWVzdCwgcmVkaXJlY3QsIHVybF9mb3IKaW1wb3J0IHNxbGl0ZTMgIyBTUUxpdGUz44OR44OD44Kx44O844K4CgpEQVRBQkFTRV9OQU1FID0gJ2FkZHJlc3MuZGInCmFwcCA9IEZsYXNrKF9fbmFtZV9fKQoKCiMgW+ODmOODq+ODkemWouaVsF0gU1FM44KS5a6f6KGM44GZ44KLCmRlZiBleGVjdXRlX3NxbChzcWwpOgogICAgY29uID0gc3FsaXRlMy5jb25uZWN0KERBVEFCQVNFX05BTUUpCiAgICBjdXIgPSBjb24uY3Vyc29yKCkKICAgIHJlc3VsdCA9IFtdCgogICAgZm9yIHJvdyBpbiBjdXIuZXhlY3V0ZShzcWwpOgogICAgICAgIHJlc3VsdC5hcHBlbmQocm93KQoKICAgIGNvbi5jb21taXQoKQogICAgY29uLmNsb3NlKCkKCiAgICByZXR1cm4gcmVzdWx0CgoKIyBb44OY44Or44OR6Zai5pWwXSBTRUxFQ1TmlofjgafluLDjgaPjgabjgY3jgZ/jg4fjg7zjgr/jga7phY3liJfjgpLpgKPmg7PphY3liJfjgavlpInmj5vjgZnjgosKIyDigLsg44OH44O844K/44OZ44O844K55qeL6YCg44Gr5L6d5a2Y44GZ44KLCmRlZiBjb252ZXJ0X3RibF9hZGRyZXNzKHJhd19yb3cpOgogICAgcmV0dXJuKHsKICAgICAgICAnaWQnOiByYXdfcm93WzBdLAogICAgICAgICduYW1lJzogcmF3X3Jvd1sxXSwKICAgICAgICAnbmFtZV95b21pJzogcmF3X3Jvd1syXSwKICAgICAgICAncG9zdGFsX2FkZHJlc3MnOiByYXdfcm93WzNdLAogICAgICAgICdtZW1vJzogcmF3X3Jvd1s0XQogICAgfSkKCgojIOODh+ODvOOCv+S4gOimp++8iOODiOODg+ODl+ODmuODvOOCuO+8iQpAYXBwLnJvdXRlKCcvJywgbWV0aG9kcz1bJ0dFVCddKQpkZWYgc2hvdygpOgogICAgdXNlcl9kYXRhID0gW10KCiAgICBmb3IgZGF0YSBpbiBleGVjdXRlX3NxbCgnU0VMRUNUIGlkLCBuYW1lLCBuYW1lX3lvbWksIHBvc3RhbF9hZGRyZXNzLCBtZW1vIEZST00gdGJsX2FkZHJlc3MnKToKICAgICAgICB1c2VyX2RhdGEuYXBwZW5kKGNvbnZlcnRfdGJsX2FkZHJlc3MoZGF0YSkpCgogICAgcmV0dXJuIHJlbmRlcl90ZW1wbGF0ZSgnaW5kZXguaHRtbCcsIHVzZXJfZGF0YT11c2VyX2RhdGEpCiMgLS0tICgxKSB0ZW1wbGF0ZXMvdGVtcGxhdGUuaHRtbAojIC0tLSAgICAgdGVtcGxhdGVzL2luZGV4Lmh0bWwg44KS5L2c5oiQ44GX44CBCiMgLS0tIGFkZHJlc3MucHkg44KS44GT44GT44G+44Gn5L2c5oiQ44GX44Gm5a6f6KGM44GX44CB44OH44O844K/44Gu5LiA6Kan44GM6KGo5b2i5byP44Gn6KGo56S644GV44KM44KL44GT44Go44KS56K66KqNCgoKIyBb5Yem55CGXSDjg4fjg7zjgr/mjL/lhaUKQGFwcC5yb3V0ZSgnLycsIG1ldGhvZHM9WydQT1NUJ10pCmRlZiBpbnNlcnQoKToKICAgIG5hbWUgPSByZXF1ZXN0LmZvcm1bJ25hbWUnXQogICAgbmFtZV95b21pID0gcmVxdWVzdC5mb3JtWyduYW1lX3lvbWknXQogICAgYWRkcmVzcyA9IHJlcXVlc3QuZm9ybVsncG9zdGFsX2FkZHJlc3MnXQogICAgbWVtbyA9IHJlcXVlc3QuZm9ybVsnbWVtbyddCgogICAgZXhlY3V0ZV9zcWwoZidJTlNFUlQgSU5UTyB0YmxfYWRkcmVzcyAobmFtZSwgbmFtZV95b21pLCBwb3N0YWxfYWRkcmVzcywgbWVtbykgVkFMVUVTICgie25hbWV9IiwgIntuYW1lX3lvbWl9IiwgInthZGRyZXNzfSIsICJ7bWVtb30iKScpCgogICAgcmV0dXJuIHNob3coKQojIC0tLSAoMikgYWRkcmVzcy5weSDjgpLjgZPjgZPjgb7jgafkvZzmiJDjgZfjgablrp/ooYzjgZfjgIHjg4fjg7zjgr/jga7mjL/lhaXjgYzjgafjgY3jgovjgZPjgajjgpLnorroqo0KCgojIOips+e0sOODmuODvOOCuApAYXBwLnJvdXRlKCcvZGV0YWlsJywgbWV0aG9kcz1bJ1BPU1QnXSkKZGVmIGRldGFpbCgpOgogICAgaWQgPSByZXF1ZXN0LmZvcm1bJ2lkJ10KICAgICMgMeihjOOBoOOBkeOBl+OBi+i/lOOCieOBquOBhOOBr+OBmuOBquOBruOBp+OAgVswXeOCkuaMh+WumuOBl+OBpuOBiuOBjyAo44GT44KT44Gq44Kk44Oh44O844K4OiBbWzEsMiwzXV0g4oaSIFsxLDIsM10pCiAgICByb3dfcmF3ID0gZXhlY3V0ZV9zcWwoZidTRUxFQ1QgKiBGUk9NIHRibF9hZGRyZXNzIFdIRVJFIGlkID0ge2lkfScpWzBdCiAgICBkYXRhID0gY29udmVydF90YmxfYWRkcmVzcyhyb3dfcmF3KQoKICAgIHJldHVybiByZW5kZXJfdGVtcGxhdGUoJ2RldGFpbC5odG1sJywgZGF0YT1kYXRhKQojIC0tLSAoMykgdGVtcGxhdGVzL2RldGFpbC5odG1sIOOCkuS9nOaIkOOBl+OAgQojIGFkZHJlc3MucHkg44KS44GT44GT44G+44Gn5L2c5oiQ44GX44Gm6Kmz57Sw44Oa44O844K444GM6KGo56S644Gn44GN44KL44GT44Go44KS56K66KqNCgoKIyBb5Yem55CGXSDjg4fjg7zjgr/lh6bnkIYKQGFwcC5yb3V0ZSgnL2RlbGV0ZScsIG1ldGhvZHM9WydQT1NUJ10pCmRlZiBkZWxldGUoKToKICAgIGlkID0gcmVxdWVzdC5mb3JtWydpZCddCiAgICBleGVjdXRlX3NxbChmJ0RFTEVURSBGUk9NIHRibF9hZGRyZXNzIFdIRVJFIGlkID0ge2lkfScpCgogICAgcmV0dXJuIHJlZGlyZWN0KHVybF9mb3IoJ3Nob3cnKSkKIyAtLS0gKDQpIGFkZHJlc3MucHkg44KS44GT44GT44G+44Gn5L2c5oiQ44GX44Gm5a6f6KGM44GX44CBCiMgICAgICAgICDjg4fjg7zjgr/jga7liYrpmaTjgYzjgafjgY3jgovjgZPjgajjgpLnorroqo0KCgojIFvlh6bnkIZdIOODh+ODvOOCv+abtOaWsApAYXBwLnJvdXRlKCcvdXBkYXRlJywgbWV0aG9kcz1bJ1BPU1QnXSkKZGVmIHVwZGF0ZSgpOgogICAgaWQgPSByZXF1ZXN0LmZvcm1bJ2lkJ10KICAgIG5hbWUgPSByZXF1ZXN0LmZvcm1bJ25hbWUnXQogICAgbmFtZV95b21pID0gcmVxdWVzdC5mb3JtWyduYW1lX3lvbWknXQogICAgcG9zdGFsX2FkZHJlc3MgPSByZXF1ZXN0LmZvcm1bJ3Bvc3RhbF9hZGRyZXNzJ10KICAgIG1lbW8gPSByZXF1ZXN0LmZvcm1bJ21lbW8nXQoKICAgIGV4ZWN1dGVfc3FsKGYnVVBEQVRFIHRibF9hZGRyZXNzIFNFVCBuYW1lID0gIntuYW1lfSIsIG5hbWVfeW9taSA9ICJ7bmFtZV95b21pfSIsIHBvc3RhbF9hZGRyZXNzID0gIntwb3N0YWxfYWRkcmVzc30iLCBtZW1vID0gInttZW1vfSIgV0hFUkUgaWQgPSB7aWR9JykKCiAgICByZXR1cm4gcmVkaXJlY3QodXJsX2Zvcignc2hvdycpKQojIC0tLSAoNSkgYWRkcmVzcy5weSDjgpLjgZPjgZPjgb7jgafkvZzmiJDjgZfjgablrp/ooYzjgZcKIyAgICAgICAgIOODh+ODvOOCv+OBruabtOaWsOOBjOOBp+OBjeOCi+OBk+OBqOOCkueiuuiqjQ==',
      },
      {
        'type': 'sqlite',
        'name': 'address.db'
      },
      {
        'type': 'directory',
        'name': 'templates',
        'files': [
          {
            'type': 'file',
            'name': 'index.html',
            'content': b'eyUgZXh0ZW5kcyAndGVtcGxhdGUuaHRtbCcgJX0KeyUgYmxvY2sgbWFpbiAlfQo8aDE+44Ki44OJ44Os44K55LiA6KanPC9oMT4KPHRhYmxlIHN0eWxlPSJib3JkZXItc3R5bGU6IHNvbGlkIj4KPHRyPgogICAgPHRoPmlkPC90aD4KICAgIDx0aD7lkI3liY08L3RoPgogICAgPHRoPuWQjeWJjSjjgojjgb/jgYzjgaopPC90aD4KICAgIDx0aD7kvY/miYA8L3RoPgogICAgPHRoPuODoeODojwvdGg+CiAgICA8dGg+PC90aD4KPC90cj4KCnslIGZvciBkYXRhIGluIHVzZXJfZGF0YSAlfQo8dHI+CiAgICA8dGQ+e3sgZGF0YVsnaWQnXSB9fTwvdGQ+CiAgICA8dGQ+e3sgZGF0YVsnbmFtZSddIH19PC90ZD4KICAgIDx0ZD57eyBkYXRhWyduYW1lX3lvbWknXSB9fTwvdGQ+CiAgICA8dGQ+e3sgZGF0YVsncG9zdGFsX2FkZHJlc3MnXSB9fTwvdGQ+CiAgICA8dGQ+e3sgZGF0YVsnbWVtbyddIH19PC90ZD4KICAgIDx0ZD4KICAgICAgICA8Zm9ybSBtZXRob2Q9InBvc3QiIGFjdGlvbj0iZGV0YWlsIj4KICAgICAgICAgICAgPGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iaWQiIHZhbHVlPSJ7eyBkYXRhWydpZCddIH19Ij4KICAgICAgICAgICAgPGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9Iuips+e0sCI+CiAgICAgICAgPC9mb3JtPgogICAgPC90ZD4KPC90cj4KeyUgZW5kZm9yICV9Cgo8dHI+CiAgICA8dGQ+e3sgdXNlcl9kYXRhIHwgbGVuZ3RoICsgMSB9fTwvdGQ+CiAgICA8dGQ+PGlucHV0IGZvcm09Imluc2VydCIgbmFtZT0ibmFtZSIgcmVxdWlyZWQgcGxhY2Vob2xkZXI9IuWQjeWJjSI+PC90ZD4KICAgIDx0ZD48aW5wdXQgZm9ybT0iaW5zZXJ0IiBuYW1lPSJuYW1lX3lvbWkiIHJlcXVpcmVkIHBsYWNlaG9sZGVyPSLlkI3liY3vvIjjgojjgb/jgYzjgaopICI+PC90ZD4KICAgIDx0ZD48aW5wdXQgZm9ybT0iaW5zZXJ0IiBuYW1lPSJwb3N0YWxfYWRkcmVzcyIgcmVxdWlyZWQgcGxhY2Vob2xkZXI9IuS9j+aJgCI+PC90ZD4KICAgIDx0ZD48aW5wdXQgZm9ybT0iaW5zZXJ0IiBuYW1lPSJtZW1vIiByZXF1aXJlZCBwbGFjZWhvbGRlcj0i44Oh44OiIj48L3RkPgogICAgPHRkPgogICAgICAgIDxmb3JtIGFjdGlvbj0iLyIgaWQ9Imluc2VydCIgbWV0aG9kPSJwb3N0Ij4KICAgICAgICAgICAgPGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9Iui/veWKoCI+CiAgICAgICAgPC9mb3JtPgogICAgPC90ZD4KPC90ZD4KPC90YWJsZT4KeyUgZW5kYmxvY2sgJX0=',
          },
          {
            'type': 'file',
            'name': 'template.html',
            'content': b'PCFET0NUWVBFIGh0bWw+CjxodG1sPgogICAgPGhlYWQ+CiAgICAgICAgPG1ldGEgY2hhcnNldD0iVVRGLTgiIC8+CiAgICAgICAgPHRpdGxlPkFkZHJlc3MgYm9vayBvbiBTUUxpdGU8L3RpdGxlPgogICAgICAgIDxzdHlsZT4KICAgICAgICAgICAgdGFibGUsIHRoLCB0ZHsKICAgICAgICAgICAgICAgIGJvcmRlci1jb2xsYXBzZTogY29sbGFwc2U7CiAgICAgICAgICAgICAgICBib3JkZXI6IHNvbGlkOwogICAgICAgICAgICB9CiAgICAgICAgPC9zdHlsZT4KICAgIDwvaGVhZD4KICAgIDxib2R5PgogICAgPGhlYWRlcj4KICAgICAgICA8aDE+U1FMaXRlMyDkvY/miYDpjLI8L2gxPgogICAgICAgIDxoMj4tLS08L2gyPgogICAgPC9oZWFkZXI+CiAgICA8aHIgLz4KICAgIHslIGJsb2NrIG1haW4gJX0KICAgIHslIGVuZGJsb2NrICV9CiAgICA8aHIgLz4KICAgIDwvbWFpbj4KICAgIDxmb290ZXIgY2xhc3M9InRkLWZvb3RlciI+CiAgICAgICAgPGFkZHJlc3M+Q29weXJpZ2h0IChjKSAyMDIxIC0tLTwvYWRkcmVzcz4KICAgIDwvZm9vdGVyPgogICAgPC9ib2R5Pgo8aHRtbD4=',
          },
          {
            'type': 'file',
            'name': 'detail.html',
            'content': b'eyUgZXh0ZW5kcyAndGVtcGxhdGUuaHRtbCcgJX0KeyUgYmxvY2sgbWFpbiAlfQo8aDE+44OX44Ot44OV44Kj44O844Or6Kmz57SwPC9oPgo8YSBocmVmPSIvIj4KPGJ1dHRvbiBzdHlsZT0ibWFyZ2luOjEwcHggMCI+4oaQIOS4gOimp+OBq+aIu+OCizwvYnV0dG9uPgo8L2E+Cjx0YWJsZT4KPHRyPjx0aD5pZDwvdGQ+PHRkPnt7ZGF0YVsnaWQnXX19PC90aD48L3RyPgo8dHI+PHRoPuWQjeWJjTwvdGQ+PHRkPjxpbnB1dCBuYW1lPSJuYW1lIiB2YWx1ZT0ie3tkYXRhWyduYW1lJ119fSIgZm9ybT0idXBkYXRlX2Zvcm0iPjwvdGg+PC90cj4KPHRyPgogICAgPHRkPuWQjeWJjSAo44KI44G/44GM44GqKSA8L3RkPjx0ZD48aW5wdXQgbmFtZT0ibmFtZV95b21pIiB2YWx1ZT0ie3tkYXRhWyduYW1lX3lvbWknXX19IiBmb3JtPSJ1cGRhdGVfZm9ybSI+PC90ZD4KPC90cj4KPHRyPgogICAgPHRkPuS9j+aJgDwvdGQ+PHRkPjxpbnB1dCBuYW1lPSJwb3N0YWxfYWRkcmVzcyIgdmFsdWU9Int7ZGF0YVsncG9zdGFsX2FkZHJlc3MnXX19IiBmb3JtPSJ1cGRhdGVfZm9ybSI+PC90ZD4KPC90cj4KPHRyPgogICAgPHRkPuODoeODojwvdGQ+PHRkPjxpbnB1dCBuYW1lPSJtZW1vIiB0eXBlPSJ0ZXh0Ym94IiB2YWx1ZT0ie3tkYXRhWydtZW1vJ119fSIgZm9ybT0idXBkYXRlX2Zvcm0iPjwvdGQ+CjwvdHI+CjwvdGFibGU+Cjxmb3JtIG1ldGhvZD0icG9zdCIgYWN0aW9uPSIvZGVsZXRlIiBzdHlsZT0iZGlzcGxheTppbmxpbmUiPgogICAgPGlucHV0IHR5cGU9ImhpZGRlbiIgbmFtZT0iaWQiIHZhbHVlPSJ7eyBkYXRhWydpZCddfX0iPgogICAgPGlucHV0IHR5cGU9InN1Ym1pdCIgdmFsdWU9IuWJiumZpCIgc3R5bGU9ImJhY2tncm91bmQtY29sb3I6IHJlZCI+CjwvZm9ybT4KPGZvcm0gbWV0aG9kPSJwb3N0IiBhY3Rpb249Ii91cGRhdGUiIHN0eWxlPSJkaXNwbGF5OmlubGluZSIgaWQ9InVwZGF0ZV9mb3JtIj4KICAgIDxpbnB1dCB0eXBlPSJoaWRkZW4iIG5hbWU9ImlkIiB2YWx1ZT0ie3sgZGF0YVsnaWQnXX19Ij4KICAgIDxpbnB1dCB0eXBlPSJzdWJtaXQiIHZhbHVlPSLmm7TmlrAiPgo8L2Zvcm0+CnslIGVuZGJsb2NrICV9',
          },
        ],
      },
    ],
  ]

file_tree_errors = []

def diff_file_and_content(filepath, content):
  file = open(filepath, 'r')
  d = difflib.Differ()
  diff = d.compare(base64.b64decode(content).decode().splitlines(keepends=True), file.readlines())
  file.close()
  return diff

def file_exist_check(files, basedir = '.'):
  for file in files:
    filepath = basedir + '/' + file['name']

    if file['type'] == 'directory':
      if (not os.path.isdir(filepath)):
        file_tree_errors.append('フォルダ「{}」が存在しません。'.format(filepath))
      file_exist_check(file['files'], filepath)

    elif file['type'] == 'file':
      if (os.path.isfile(filepath)):
        diff = diff_file_and_content(filepath, file['content'])
        output = open(filepath + '.diff', 'w')
        output.writelines('\n'.join(diff))
        output.close()
      else:
        file_tree_errors.append('ファイル「{}」が存在しません。'.format(filepath))
    
    elif file['type'] == 'sqlite':
      if (not os.path.isfile(filepath)):
        file_tree_errors.append('SQLiteのデータベースファイル「{}」が存在しません。'.format(filepath))

    else: 
      raise SyntaxError('スクリプトに問題があります。')

def main(no):
  if no == None:
    raise ValueError('引数を指定してください。')
  if no not in range(1, len(tree) + 1):
    raise ValueError('問題番号が不正です。')
  
  file_exist_check(tree[no - 1])

if __name__ == '__main__':
  no = input('問題番号を入力してください : ')

  print('\nカレントディレクトリ: {}\n'.format(os.path.dirname(os.path.abspath(__file__))))

  main(int(no))

  if len(file_tree_errors) > 0:
    print('\nファイル構造に問題があります。')
    for error in file_tree_errors:
      print('・' + error)
  else:
    print('\nファイル構造に問題はありません。')
  
  print('\nファイル差分を出力しました。')
  print()