{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "e2025bdc-cc90-4706-bc91-95e430ec04af",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr></tr></thead><tbody></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [],
       "datasetInfos": [
        {
         "name": "_sqldf",
         "schema": {
          "fields": [],
          "type": "struct"
         },
         "tableIdentifier": null,
         "typeStr": "pyspark.sql.connect.dataframe.DataFrame"
        }
       ],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {
        "createTempViewForImplicitDf": true,
        "dataframeName": "_sqldf",
        "executionCount": 2
       },
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%sql\n",
    "CREATE CATALOG IF NOT EXISTS `ecom-medallion-pipeline`;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "d327bd4d-19c3-473c-8dfb-db317bc612b7",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr></tr></thead><tbody></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [],
       "datasetInfos": [
        {
         "name": "_sqldf",
         "schema": {
          "fields": [],
          "type": "struct"
         },
         "tableIdentifier": null,
         "typeStr": "pyspark.sql.connect.dataframe.DataFrame"
        }
       ],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {
        "createTempViewForImplicitDf": true,
        "dataframeName": "_sqldf",
        "executionCount": 3
       },
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%sql\n",
    "CREATE SCHEMA IF NOT EXISTS `ecom-medallion-pipeline`.raw;\n",
    "CREATE SCHEMA IF NOT EXISTS `ecom-medallion-pipeline`.bronze;\n",
    "CREATE SCHEMA IF NOT EXISTS `ecom-medallion-pipeline`.silver;\n",
    "CREATE SCHEMA IF NOT EXISTS `ecom-medallion-pipeline`.gold;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "46f8ed83-27e8-4bf1-bd09-1015238a7269",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr></tr></thead><tbody></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [],
       "datasetInfos": [
        {
         "name": "_sqldf",
         "schema": {
          "fields": [],
          "type": "struct"
         },
         "tableIdentifier": null,
         "typeStr": "pyspark.sql.connect.dataframe.DataFrame"
        }
       ],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {
        "createTempViewForImplicitDf": true,
        "dataframeName": "_sqldf",
        "executionCount": 4
       },
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%sql\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.raw.mobile_orders;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "befd9dfc-877d-4032-bb81-e15328f72829",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr></tr></thead><tbody></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [],
       "datasetInfos": [
        {
         "name": "_sqldf",
         "schema": {
          "fields": [],
          "type": "struct"
         },
         "tableIdentifier": null,
         "typeStr": "pyspark.sql.connect.dataframe.DataFrame"
        }
       ],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {
        "createTempViewForImplicitDf": true,
        "dataframeName": "_sqldf",
        "executionCount": 5
       },
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%sql\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.bronze.mobile_orders;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "3bb7ca76-91ce-4630-a5f5-affc64717e36",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr></tr></thead><tbody></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [],
       "datasetInfos": [
        {
         "name": "_sqldf",
         "schema": {
          "fields": [],
          "type": "struct"
         },
         "tableIdentifier": null,
         "typeStr": "pyspark.sql.connect.dataframe.DataFrame"
        }
       ],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {
        "createTempViewForImplicitDf": true,
        "dataframeName": "_sqldf",
        "executionCount": 6
       },
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%sql\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.silver.mobile_orders;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {
    "application/vnd.databricks.v1+cell": {
     "cellMetadata": {
      "byteLimit": 2048000,
      "implicitDf": true,
      "rowLimit": 10000
     },
     "inputWidgets": {},
     "nuid": "87260a2e-9db3-435b-b768-8b26be27cbc7",
     "showTitle": false,
     "tableResultSettingsMap": {},
     "title": ""
    }
   },
   "outputs": [
    {
     "output_type": "display_data",
     "data": {
      "text/html": [
       "<style scoped>\n",
       "  .table-result-container {\n",
       "    max-height: 300px;\n",
       "    overflow: auto;\n",
       "  }\n",
       "  table, th, td {\n",
       "    border: 1px solid black;\n",
       "    border-collapse: collapse;\n",
       "  }\n",
       "  th, td {\n",
       "    padding: 5px;\n",
       "  }\n",
       "  th {\n",
       "    text-align: left;\n",
       "  }\n",
       "</style><div class='table-result-container'><table class='table-result'><thead style='background-color: white'><tr></tr></thead><tbody></tbody></table></div>"
      ]
     },
     "metadata": {
      "application/vnd.databricks.v1+output": {
       "addedWidgets": {},
       "aggData": [],
       "aggError": "",
       "aggOverflow": false,
       "aggSchema": [],
       "aggSeriesLimitReached": false,
       "aggType": "",
       "arguments": {},
       "columnCustomDisplayInfos": {},
       "data": [],
       "datasetInfos": [
        {
         "name": "_sqldf",
         "schema": {
          "fields": [],
          "type": "struct"
         },
         "tableIdentifier": null,
         "typeStr": "pyspark.sql.connect.dataframe.DataFrame"
        }
       ],
       "dbfsResultPath": null,
       "isJsonSchema": true,
       "metadata": {
        "createTempViewForImplicitDf": true,
        "dataframeName": "_sqldf",
        "executionCount": 7
       },
       "overflow": false,
       "plotOptions": {
        "customPlotOptions": {},
        "displayType": "table",
        "pivotAggregation": null,
        "pivotColumns": null,
        "xColumns": null,
        "yColumns": null
       },
       "removedWidgets": [],
       "schema": [],
       "type": "table"
      }
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "%sql\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.gold.price_segments;\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.gold.brand_summary;\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.gold.top_rated_phones;"
   ]
  }
 ],
 "metadata": {
  "application/vnd.databricks.v1+notebook": {
   "computePreferences": null,
   "dashboards": [],
   "environmentMetadata": {
    "base_environment": "",
    "environment_version": "5"
   },
   "inputWidgetPreferences": null,
   "language": "python",
   "notebookMetadata": {
    "mostRecentlyExecutedCommandWithImplicitDF": {
     "commandId": 7289605264995974,
     "dataframes": [
      "_sqldf"
     ]
    },
    "pythonIndentUnit": 4
   },
   "notebookName": "CATALOG_&_SCHEMA_CREATION",
   "widgets": {}
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}
