'''
Module for crating folium map.
'''

from random import choice, random
import folium as flm

def create_map(cord_nms: tuple):
    '''
    Creates a folium map.
Returns 'Success!!!' if there was no problems.
    '''
    try:
        map_folium = flm.Map(zoom_start = 10)
        figure = flm.FeatureGroup(name = 'Json map.')
        for coordinates, name in cord_nms:
            figure.add_child(flm.CircleMarker(
                                        location = coordinates[-1],
                                        radius = random() * 20,
                                        color = choice(['yellow', 'green', 'red']),
                                        fill_color = choice(['yellow', 'green', 'red']),
                                        icon = flm.Icon(icon = 'cloud'),
                                        popup = name,
                                        fill_opacity = random()
                                              ))

        map_folium.add_child(figure)
        map_folium.add_child(flm.LayerControl())
        map_folium.save('templates/map/JSON_map.html')

    except ValueError:
        return 'Error.'

    return 'Success!!!'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
