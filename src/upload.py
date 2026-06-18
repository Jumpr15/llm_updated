from nets.transformer import LightningTransformer

# set model checkpoint
model = LightningTransformer.load_from_checkpoint("./model_ckpts/")

model.push_to_hub("Jumpr/tinystories_updated")