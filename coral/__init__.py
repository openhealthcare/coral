"""
coral - Our Opal Application
"""
from opal.core import application
from opal.core import menus

class Application(application.OpalApplication):

    default_episode_category = 'Episode'

    javascripts   = [
        'js/coral/routes.js',
        'js/coral/diagnosis_record.js',
        'js/coral/new_episode_controller.js',
    ]

    styles = [
        'css/coral.css'
    ]

    @classmethod
    def get_menu_items(klass, user=None):

        menuitems = [
            # menus.MenuItem(
            #     href="/#/list/", activepattern="/list/",
            #     icon="fa-table", display="Lists",
            #     index=0
            # ),
            menus.MenuItem(
                href='/pathway/#/add_patient',
                display='Add Patient',
                icon='fa fa-plus',
                activepattern='/pathway/#/add_patient'
            )
        ]
        admin = menus.MenuItem(
            href="/admin/", icon="fa-cogs", display="Admin",
            index=999
        )
        if user:
            if user.is_staff:
                menuitems.append(admin)
        return menuitems
