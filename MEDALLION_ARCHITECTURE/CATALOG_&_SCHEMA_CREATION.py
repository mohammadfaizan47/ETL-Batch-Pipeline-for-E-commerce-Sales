{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE CATALOG IF NOT EXISTS `ecom-medallion-pipeline`;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
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
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.raw.mobile_orders;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.bronze.mobile_orders;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.silver.mobile_orders;"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%sql\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.gold.price_segments;\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.gold.brand_summary;\n",
    "CREATE VOLUME IF NOT EXISTS `ecom-medallion-pipeline`.gold.top_rated_phones;"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "name": "python"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
