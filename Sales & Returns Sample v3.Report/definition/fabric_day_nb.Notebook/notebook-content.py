# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "819746b2-ee54-4268-92a1-63ee3d61670c",
# META       "default_lakehouse_name": "fabric_day_lh",
# META       "default_lakehouse_workspace_id": "3640bb1c-2807-4340-bbd4-8536ee9ee3e6",
# META       "known_lakehouses": [
# META         {
# META           "id": "819746b2-ee54-4268-92a1-63ee3d61670c"
# META         }
# META       ]
# META     }
# META   }
# META }

# MARKDOWN ********************

# ### Install the Semantic link Labs library in a Fabric notebook


# CELL ********************

%pip install semantic-link-labs

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# ### Once installed, run this code to import the library into your notebook

# CELL ********************

import sempy_labs as labs
from sempy_labs import migration, directlake, admin, graph
from sempy_labs import lakehouse as lake
from sempy_labs import report as rep
from sempy_labs.tom import connect_semantic_model
from sempy_labs.report import ReportWrapper

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************

# # Model Best Pratice Analyzer

# CELL ********************

import sempy_labs as labs

dataset = 'Sales & Returns Sample v201912' # Enter the name or ID of your semantic model
workspace = 'fabricday_ws' # Enter the name or ID of the workspace in which the semantic model resides

labs.run_model_bpa(dataset=dataset, workspace=workspace)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# MARKDOWN ********************


# MARKDOWN ********************

# import sempy_labs as labs
# 
# 
# dataset = 'Sales & Returns Sample v201912' # Enter the name or ID of your semantic model
# workspace = 'fabricday_ws' # Enter the name or ID of the workspace in which the semantic model resides
# languages = ['fr-FR']
# 
# labs.translate_semantic_model(dataset=dataset, workspace=workspace, languages=languages)

# MARKDOWN ********************

# # Vertipaq Analyzer

# CELL ********************

import sempy_labs as labs

dataset = 'Sales & Returns Sample v201912' # Enter the name or ID of your semantic model
workspace = 'fabricday_ws' # Enter the name or ID of the workspace in which the semantic model resides

x = labs.vertipaq_analyzer(dataset=dataset, workspace=workspace)
x = labs.vertipaq_analyzer(dataset=dataset, workspace=workspace, export='table') # Setting export='table' will export the results to delta tables in the lakehouse attached to the notebook
x = labs.vertipaq_analyzer(dataset=dataset, workspace=workspace, export='zip') # Setting export='zip' will export the results to a .zip file in the lakehouse attached to the notebook.


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
