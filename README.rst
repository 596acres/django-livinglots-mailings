django-livinglots-mailings
==========================

Part of 596 Acres' `Living Lots <https://github.com/596acres/django-livinglots>`_,
a Django app that sends emails based on simple criteria.

This app is currently mostly used to email participants after a certain amount
of time that they have been active on the site. Living Lots also sends
notifications to site facilitators and managers via `django-livinglots-notify
<https://github.com/596acres/django-livinglots-notify>`_ and to participants
through `django-livinglots-organize
<https://github.com/596acres/django-livinglots-organize>`_.

This app could easily be extended to send more email in response to more 
complex conditions. See `models.py` and `mailers.py`.


License
-------

django-livinglots-mailings is released under the GNU `Affero General Public 
License, version 3 <http://www.gnu.org/licenses/agpl.html>`_.
