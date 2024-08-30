
# === Configuration options ===

def set_config(c):
    c.input_path                   = "/users/mleblan6/.energyflow/datasets/QG_jets.npz"
    #c.input_path                   = "/users/mleblan6/.energyflow/datasets/top_qcd_0.npz"
    #c.input_path                   = "data/qgtag/QG_jets.npz"
    c.data_dimension               = 2
    c.compression_ratio            = 16.0
    c.apply_normalization          = False
    c.model_name                   = "AE"
    c.epochs                       = 300
    c.lr                           = 0.001
    c.batch_size                   = 512 # was 512
    c.early_stopping               = True
    c.lr_scheduler                 = True




# === Additional configuration options ===

    c.early_stopping_patience      = 50
    c.min_delta                    = 0
    c.lr_scheduler_patience        = 50
    c.custom_norm                  = False
    c.l1                           = True
    c.reg_param                    = 0.001
    c.RHO                          = 0.05
    c.test_size                    = 0.15 # was 0
    # c.number_of_columns            = 24
    # c.latent_space_size            = 12
    c.extra_compression            = False
    c.intermittent_model_saving    = False
    c.intermittent_saving_patience = 100
    c.activation_extraction        = True
