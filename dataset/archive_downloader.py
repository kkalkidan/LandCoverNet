
from radiant_mlhub import client



collection_id = 'ref_landcovernet_v1_source'

client.download_archive(collection_id, output_dir='../data/Landcovernet_archive')