from netsquid.components.models.delaymodels import FibreDelayModel, GaussianDelayModel, FixedDelayModel
from netsquid.components.models.qerrormodels import FibreLossModel

def get_delay_model(name, **kwargs):
    if name == "FibreDelayModel":
        return FibreDelayModel(**kwargs)
    if name == "FixedDelayModel":
        return FixedDelayModel(**kwargs)
    if name == "GaussianDelayModel":
        return GaussianDelayModel(**kwargs)
    pass

def get_loss_model(name, **kwargs):
    if name == "FibreLossModel":
        return FibreLossModel(**kwargs)
    pass
