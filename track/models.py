from django.db import models

class Track(models.Model):
    container_number = models.CharField(max_length=100, null=True, blank=True)
    hbl_number = models.CharField(max_length=100, null=True, blank=True)
    mbl_number = models.CharField(max_length=100, null=True, blank=True)

    shipper = models.CharField(max_length=100, null=True, blank=True)
    consignee = models.CharField(max_length=100, null=True, blank=True)
    vessel_name = models.CharField(max_length=100, null=True, blank=True)
    voyage_number = models.CharField(max_length=100, null=True, blank=True)

    port_of_loading = models.CharField(max_length=100, null=True, blank=True)
    port_of_discharge = models.CharField(max_length=100, null=True, blank=True)
    dispatched_date = models.DateField(null=True, blank=True)
    transit_port = models.CharField(max_length=100, null=True, blank=True)
    arrival_date_to_transit_port = models.DateField(null=True, blank=True)
    dispatch_date_to_final_port = models.DateField(null=True, blank=True)
    load_on_rail = models.DateField(null=True, blank=True)
    arrival_to_final_destination = models.DateField(null=True, blank=True)
    date_of_arriving_to_warehouse = models.DateField(null=True, blank=True)
    pick_up_date_of_warehouse = models.DateField(null=True, blank=True)
    steam_release_status = models.CharField(max_length=100, null=True, blank=True)
    delivery_status = models.CharField(max_length=100, null=True, blank=True)
    customs_release_status = models.CharField(max_length=100, null=True, blank=True)