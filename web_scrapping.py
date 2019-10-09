
Web Scrapping  practice in Python
In [1]:
import requests as rq
from BeautifulSoap import bs4
In [2]:
r = rq.get('https://en.wikipedia.org/wiki/List_of_cities_in_India_by_population')
In [3]:
r.status_code
Out[3]:
200
In [4]:
soup = bs4.BeautifulSoup(r.content, 'html.parser',xml)
In [5]:
soup.title.text
Out[5]:
'List of cities in India by population - Wikipedia'
In [6]:
table = soup.findAll('table', attrs = {'class':'wikitable'})
In [7]:
soup.p
Out[7]:
<p>
The following tables are the <b>list of cities in <a href="/wiki/India" title="India">India</a></b> by population. Often cities are bifurcated into multiple regions (municipalities) which results in creation of cities within cities which may figure in the list. The entire work of this article is based on <i><a class="mw-redirect" href="/wiki/Census_of_India,_2011" title="Census of India, 2011">Census of India, 2011</a></i>, conducted by the <i>Office of the Registrar General and Census Commissioner</i>, under <a href="/wiki/Ministry_of_Home_Affairs_(India)" title="Ministry of Home Affairs (India)">Ministry of Home Affairs (India)</a>, <a href="/wiki/Government_of_India" title="Government of India">Government of India</a>.
</p>
In [8]:
len(table)
Out[8]:
12
In [9]:
tb = []
for i in table:
    x = i.findAll('tbody')
    tb.append(x)
In [10]:
tb
Out[10]:
[[<tbody><tr>
  <th style="width:5%;">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-0"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>1</td>
  <td><b><a href="/wiki/Mumbai" title="Mumbai">Mumbai</a></b></td>
  <td>12,442,373</td>
  <td>11,978,450</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>2</td>
  <td><b><a href="/wiki/Delhi" title="Delhi">Delhi</a></b></td>
  <td>11,034,555</td>
  <td>9,879,172</td>
  <td><a href="/wiki/Delhi" title="Delhi">Delhi</a>
  </td></tr>
  <tr>
  <td>3</td>
  <td><b><a href="/wiki/Bangalore" title="Bangalore">Bangalore</a></b></td>
  <td>8,443,675</td>
  <td>4,301,326</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>4</td>
  <td><b><a class="mw-redirect" href="/wiki/Hyderabad,_India" title="Hyderabad, India">Hyderabad</a></b></td>
  <td>6,731,790</td>
  <td>3,637,483</td>
  <td><a href="/wiki/Telangana" title="Telangana">Telangana</a>
  </td></tr>
  <tr>
  <td>5</td>
  <td><a href="/wiki/Ahmedabad" title="Ahmedabad">Ahmedabad</a></td>
  <td>5,577,940</td>
  <td>3,520,085</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>6</td>
  <td><b><a href="/wiki/Chennai" title="Chennai">Chennai</a></b></td>
  <td>4,646,000</td>
  <td>4,343,645</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>7</td>
  <td><b><a href="/wiki/Kolkata" title="Kolkata">Kolkata</a> </b></td>
  <td>4,496,694</td>
  <td>4,572,876</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>8</td>
  <td><a href="/wiki/Surat" title="Surat">Surat</a></td>
  <td>4,467,797</td>
  <td>2,433,835</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>9</td>
  <td><a href="/wiki/Pune" title="Pune">Pune</a></td>
  <td>3,124,458</td>
  <td>2,538,473</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>10</td>
  <td><b><a href="/wiki/Jaipur" title="Jaipur">Jaipur</a></b></td>
  <td>3,046,163</td>
  <td>2,322,575</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr>
  <tr>
  <td>11</td>
  <td><b><a href="/wiki/Lucknow" title="Lucknow">Lucknow</a></b></td>
  <td>2,817,105</td>
  <td>2,185,927</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>12</td>
  <td><a href="/wiki/Kanpur" title="Kanpur">Kanpur</a></td>
  <td>2,765,348</td>
  <td>2,551,337</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>13</td>
  <td><a href="/wiki/Nagpur" title="Nagpur">Nagpur</a></td>
  <td>2,405,665</td>
  <td>2,052,066</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>14</td>
  <td><a href="/wiki/Indore" title="Indore">Indore</a></td>
  <td>1,964,086</td>
  <td>1,474,968</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>15</td>
  <td><a href="/wiki/Thane" title="Thane">Thane</a></td>
  <td>1,841,488</td>
  <td>1,262,551</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>16</td>
  <td><b><a href="/wiki/Bhopal" title="Bhopal">Bhopal</a></b></td>
  <td>1,798,218</td>
  <td>1,437,354</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>17</td>
  <td><a href="/wiki/Visakhapatnam" title="Visakhapatnam">Visakhapatnam</a><sup class="reference" id="cite_ref-fn1_5-0"><a href="#cite_note-fn1-5">[a]</a></sup><sup class="reference" id="cite_ref-ap_6-0"><a href="#cite_note-ap-6">[5]</a></sup></td>
  <td>1,728,128</td>
  <td>982,904</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>18</td>
  <td><a href="/wiki/Pimpri-Chinchwad" title="Pimpri-Chinchwad">Pimpri-Chinchwad</a></td>
  <td>1,727,692</td>
  <td>1,012,472</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>19</td>
  <td><b><a href="/wiki/Patna" title="Patna">Patna</a></b></td>
  <td>1,684,222</td>
  <td>1,366,444</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>20</td>
  <td><a href="/wiki/Vadodara" title="Vadodara">Vadodara</a></td>
  <td>1,670,806</td>
  <td>1,306,227</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>21</td>
  <td><a class="mw-redirect" href="/wiki/Ghaziabad,_India" title="Ghaziabad, India">Ghaziabad</a></td>
  <td>1,648,643</td>
  <td>968,256</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>22</td>
  <td><a href="/wiki/Ludhiana" title="Ludhiana">Ludhiana</a></td>
  <td>1,618,879</td>
  <td>1,398,467</td>
  <td><a class="mw-redirect" href="/wiki/Punjab_(India)" title="Punjab (India)">Punjab</a>
  </td></tr>
  <tr>
  <td>23</td>
  <td><a href="/wiki/Agra" title="Agra">Agra</a></td>
  <td>1,585,704</td>
  <td>1,275,134</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>24</td>
  <td><a href="/wiki/Nashik" title="Nashik">Nashik</a></td>
  <td>1,486,053</td>
  <td>1,077,236</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>25</td>
  <td><a href="/wiki/Faridabad" title="Faridabad">Faridabad</a></td>
  <td>1,414,050</td>
  <td>1,055,938</td>
  <td><a href="/wiki/Haryana" title="Haryana">Haryana</a>
  </td></tr></tbody>], [<tbody><tr>
  <th width="5%">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-1"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>26</td>
  <td><a href="/wiki/Meerut" title="Meerut">Meerut</a></td>
  <td>1,305,429</td>
  <td>1,039,405</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>27</td>
  <td><a href="/wiki/Rajkot" title="Rajkot">Rajkot</a></td>
  <td>1,286,678</td>
  <td>967,476</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>28</td>
  <td><a class="mw-redirect" href="/wiki/Kalyan-Dombivali" title="Kalyan-Dombivali">Kalyan-Dombivali</a></td>
  <td>1,247,327</td>
  <td>1,193,512</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>29</td>
  <td><a href="/wiki/Vasai-Virar" title="Vasai-Virar">Vasai-Virar</a></td>
  <td>1,222,390</td>
  <td>693,350</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>30</td>
  <td><a href="/wiki/Varanasi" title="Varanasi">Varanasi</a></td>
  <td>1,198,491</td>
  <td>1,091,918</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>31</td>
  <td><b><a href="/wiki/Srinagar" title="Srinagar">Srinagar</a></b></td>
  <td>1,180,570</td>
  <td>898,440</td>
  <td><a href="/wiki/Jammu_and_Kashmir" title="Jammu and Kashmir">Jammu and Kashmir</a>
  </td></tr>
  <tr>
  <td>32</td>
  <td><a href="/wiki/Aurangabad,_Maharashtra" title="Aurangabad, Maharashtra">Aurangabad</a></td>
  <td>1,175,116</td>
  <td>873,311</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>33</td>
  <td><a href="/wiki/Dhanbad" title="Dhanbad">Dhanbad</a></td>
  <td>1,162,472</td>
  <td>1,065,327</td>
  <td><a href="/wiki/Jharkhand" title="Jharkhand">Jharkhand</a>
  </td></tr>
  <tr>
  <td>34</td>
  <td><a href="/wiki/Amritsar" title="Amritsar">Amritsar</a></td>
  <td>1,132,383</td>
  <td>966,862</td>
  <td><a class="mw-redirect" href="/wiki/Punjab_(India)" title="Punjab (India)">Punjab</a>
  </td></tr>
  <tr>
  <td>35</td>
  <td><a href="/wiki/Navi_Mumbai" title="Navi Mumbai">Navi Mumbai</a></td>
  <td>1,120,547</td>
  <td>704,002</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>36</td>
  <td><a href="/wiki/Allahabad" title="Allahabad">Allahabad</a></td>
  <td>1,112,544</td>
  <td>975,393</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>37</td>
  <td><a href="/wiki/Howrah" title="Howrah">Howrah</a></td>
  <td>1,077,075</td>
  <td>1,007,532</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>38</td>
  <td><b><a href="/wiki/Ranchi" title="Ranchi">Ranchi</a></b></td>
  <td>1,073,427</td>
  <td>847,093</td>
  <td><a href="/wiki/Jharkhand" title="Jharkhand">Jharkhand</a>
  </td></tr>
  <tr>
  <td>39</td>
  <td><a href="/wiki/Gwalior" title="Gwalior">Gwalior</a></td>
  <td>1,069,276</td>
  <td>827,026</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>40</td>
  <td><a href="/wiki/Jabalpur" title="Jabalpur">Jabalpur</a></td>
  <td>1,055,525</td>
  <td>932,484</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>41</td>
  <td><a href="/wiki/Coimbatore" title="Coimbatore">Coimbatore</a></td>
  <td>1,050,721</td>
  <td>930,882</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>42</td>
  <td><a href="/wiki/Vijayawada" title="Vijayawada">Vijayawada</a></td>
  <td>1,034,358</td>
  <td>851,282</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>43</td>
  <td><a href="/wiki/Jodhpur" title="Jodhpur">Jodhpur</a></td>
  <td>1,033,918</td>
  <td>851,051</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr>
  <tr>
  <td>44</td>
  <td><a href="/wiki/Madurai" title="Madurai">Madurai</a></td>
  <td>1,017,865</td>
  <td>928,869</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>45</td>
  <td><b><a class="mw-redirect" href="/wiki/Raipur,_Chhattisgarh" title="Raipur, Chhattisgarh">Raipur</a></b></td>
  <td>1,010,087</td>
  <td>605,747</td>
  <td><a href="/wiki/Chhattisgarh" title="Chhattisgarh">Chhattisgarh</a>
  </td></tr>
  <tr>
  <td>46</td>
  <td><a href="/wiki/Kota,_Rajasthan" title="Kota, Rajasthan">Kota</a><sup class="reference" id="cite_ref-7"><a href="#cite_note-7">[6]</a></sup></td>
  <td>1,001,694</td>
  <td>694,316</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr>
  <tr>
  <td>47</td>
  <td><b><a href="/wiki/Chandigarh" title="Chandigarh">Chandigarh</a></b></td>
  <td>961,587</td>
  <td>808,515</td>
  <td><a href="/wiki/Chandigarh" title="Chandigarh">Chandigarh</a>
  </td></tr>
  <tr>
  <td>48</td>
  <td><a href="/wiki/Guwahati" title="Guwahati">Guwahati</a></td>
  <td>957,352</td>
  <td>809,895</td>
  <td><a href="/wiki/Assam" title="Assam">Assam</a>
  </td></tr>
  <tr>
  <td>49</td>
  <td><a href="/wiki/Solapur" title="Solapur">Solapur</a></td>
  <td>951,558</td>
  <td>872,478</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>50</td>
  <td><a class="mw-redirect" href="/wiki/Hubballi-Dharwad" title="Hubballi-Dharwad">Hubballi-Dharwad</a></td>
  <td>943,788</td>
  <td>786,195</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr></tbody>], [<tbody><tr>
  <th width="5%">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-2"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>51</td>
  <td><a href="/wiki/Tiruchirappalli" title="Tiruchirappalli">Tiruchirappalli</a><sup class="reference" id="cite_ref-8"><a href="#cite_note-8">[7]</a></sup></td>
  <td>916,674</td>
  <td>752,066</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>52</td>
  <td><a href="/wiki/Bareilly" title="Bareilly">Bareilly</a></td>
  <td>898,167</td>
  <td>718,395</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>53</td>
  <td><a href="/wiki/Mysore" title="Mysore">Mysore</a></td>
  <td>887,446</td>
  <td>755,379</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>54</td>
  <td><a href="/wiki/Tiruppur" title="Tiruppur">Tiruppur</a></td>
  <td>877,778</td>
  <td>344,543</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>55</td>
  <td><a href="/wiki/Gurgaon" title="Gurgaon">Gurgaon</a></td>
  <td>876,824</td>
  <td>173,542</td>
  <td><a href="/wiki/Haryana" title="Haryana">Haryana</a>
  </td></tr>
  <tr>
  <td>56</td>
  <td><a href="/wiki/Aligarh" title="Aligarh">Aligarh</a></td>
  <td>872,575</td>
  <td>669,087</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>57</td>
  <td><a href="/wiki/Jalandhar" title="Jalandhar">Jalandhar</a></td>
  <td>862,196</td>
  <td>706,043</td>
  <td><a class="mw-redirect" href="/wiki/Punjab_(India)" title="Punjab (India)">Punjab</a>
  </td></tr>
  <tr>
  <td>58</td>
  <td><b><a href="/wiki/Bhubaneswar" title="Bhubaneswar">Bhubaneswar</a></b></td>
  <td>837,737</td>
  <td>648,032</td>
  <td><a href="/wiki/Odisha" title="Odisha">Odisha</a>
  </td></tr>
  <tr>
  <td>59</td>
  <td><a href="/wiki/Salem,_Tamil_Nadu" title="Salem, Tamil Nadu">Salem</a></td>
  <td>831,038</td>
  <td>696,760</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>60</td>
  <td><a href="/wiki/Mira-Bhayandar" title="Mira-Bhayandar">Mira-Bhayandar</a></td>
  <td>814,655</td>
  <td>520,388</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>61</td>
  <td><a href="/wiki/Warangal" title="Warangal">Warangal</a><sup class="reference" id="cite_ref-9"><a href="#cite_note-9">[8]</a></sup></td>
  <td>811,844</td>
  <td>530,636</td>
  <td><a href="/wiki/Telangana" title="Telangana">Telangana</a>
  </td></tr>
  <tr>
  <td>62</td>
  <td><b><a href="/wiki/Thiruvananthapuram" title="Thiruvananthapuram">Thiruvananthapuram</a></b></td>
  <td>752,490</td>
  <td>744,983</td>
  <td><a href="/wiki/Kerala" title="Kerala">Kerala</a>
  </td></tr>
  <tr>
  <td>63</td>
  <td><a href="/wiki/Guntur" title="Guntur">Guntur</a><sup class="reference" id="cite_ref-10"><a href="#cite_note-10">[9]</a></sup></td>
  <td>743,354</td>
  <td>514,461</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>64</td>
  <td><a href="/wiki/Bhiwandi" title="Bhiwandi">Bhiwandi</a></td>
  <td>711,329</td>
  <td>598,741</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>65</td>
  <td><a href="/wiki/Saharanpur" title="Saharanpur">Saharanpur</a></td>
  <td>703,345</td>
  <td>455,754</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>66</td>
  <td><a href="/wiki/Gorakhpur" title="Gorakhpur">Gorakhpur</a></td>
  <td>671,048</td>
  <td>622,701</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>67</td>
  <td><a href="/wiki/Bikaner" title="Bikaner">Bikaner</a></td>
  <td>647,804</td>
  <td>529,690</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr>
  <tr>
  <td>68</td>
  <td><a href="/wiki/Amravati" title="Amravati">Amravati</a></td>
  <td>646,801</td>
  <td>549,510</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>69</td>
  <td><a href="/wiki/Noida" title="Noida">Noida</a></td>
  <td>642,381</td>
  <td>305,058</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>70</td>
  <td><a href="/wiki/Jamshedpur" title="Jamshedpur">Jamshedpur</a></td>
  <td>631,364</td>
  <td>573,096</td>
  <td><a href="/wiki/Jharkhand" title="Jharkhand">Jharkhand</a>
  </td></tr>
  <tr>
  <td>71</td>
  <td><a href="/wiki/Bhilai" title="Bhilai">Bhilai</a></td>
  <td>625,697</td>
  <td>556,366</td>
  <td><a href="/wiki/Chhattisgarh" title="Chhattisgarh">Chhattisgarh</a>
  </td></tr>
  <tr>
  <td>72</td>
  <td><a href="/wiki/Cuttack" title="Cuttack">Cuttack</a></td>
  <td>606,007</td>
  <td>534,654</td>
  <td><a href="/wiki/Odisha" title="Odisha">Odisha</a>
  </td></tr>
  <tr>
  <td>73</td>
  <td><a href="/wiki/Firozabad" title="Firozabad">Firozabad</a></td>
  <td>603,797</td>
  <td>279,102</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>74</td>
  <td><a class="mw-redirect" href="/wiki/Kochi,_India" title="Kochi, India">Kochi</a></td>
  <td>601,574</td>
  <td>596,473</td>
  <td><a href="/wiki/Kerala" title="Kerala">Kerala</a>
  </td></tr></tbody>], [<tbody><tr>
  <th width="5%">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-3"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>75</td>
  <td><a href="/wiki/Nellore" title="Nellore">Nellore</a><sup class="reference" id="cite_ref-11"><a href="#cite_note-11">[10]</a></sup><sup class="reference" id="cite_ref-city_12-0"><a href="#cite_note-city-12">[11]</a></sup></td>
  <td>600,869</td>
  <td>378,428</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>76</td>
  <td><a href="/wiki/Bhavnagar" title="Bhavnagar">Bhavnagar</a></td>
  <td>593,768</td>
  <td>511,085</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>77</td>
  <td><b><a href="/wiki/Dehradun" title="Dehradun">Dehradun</a></b></td>
  <td>578,420</td>
  <td>426,674</td>
  <td><a href="/wiki/Uttarakhand" title="Uttarakhand">Uttarakhand</a>
  </td></tr>
  <tr>
  <td>78</td>
  <td><a class="mw-redirect" href="/wiki/Durgapur,_West_Bengal" title="Durgapur, West Bengal">Durgapur</a></td>
  <td>566,937</td>
  <td>493,405</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>79</td>
  <td><a href="/wiki/Asansol" title="Asansol">Asansol</a></td>
  <td>564,491</td>
  <td>475,439</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>80</td>
  <td><a href="/wiki/Rourkela" title="Rourkela">Rourkela</a></td>
  <td>552,734</td>
  <td>426,354</td>
  <td><a href="/wiki/Odisha" title="Odisha">Odisha</a>
  </td></tr>
  <tr>
  <td>81</td>
  <td><a href="/wiki/Nanded" title="Nanded">Nanded</a></td>
  <td>550,564</td>
  <td>430,733</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>82</td>
  <td><a href="/wiki/Kolhapur" title="Kolhapur">Kolhapur</a></td>
  <td>549,283</td>
  <td>493,167</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>83</td>
  <td><a href="/wiki/Ajmer" title="Ajmer">Ajmer</a></td>
  <td>542,580</td>
  <td>485,575</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr>
  <tr>
  <td>84</td>
  <td><a class="mw-redirect" href="/wiki/Akola_city" title="Akola city">Akola</a></td>
  <td>537,149</td>
  <td>400,520</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>85</td>
  <td><a href="/wiki/Gulbarga" title="Gulbarga">Gulbarga</a></td>
  <td>532,031</td>
  <td>422,569</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>86</td>
  <td><a href="/wiki/Jamnagar" title="Jamnagar">Jamnagar</a></td>
  <td>529,308</td>
  <td>443,518</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>87</td>
  <td><a href="/wiki/Ujjain" title="Ujjain">Ujjain</a></td>
  <td>515,215</td>
  <td>430,427</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>88</td>
  <td><a class="mw-redirect" href="/wiki/Loni,_India" title="Loni, India">Loni</a></td>
  <td>512,296</td>
  <td>120,945</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>89</td>
  <td><a href="/wiki/Siliguri" title="Siliguri">Siliguri</a></td>
  <td>509,709</td>
  <td>472,374</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>90</td>
  <td><a href="/wiki/Jhansi" title="Jhansi">Jhansi</a></td>
  <td>507,293</td>
  <td>383,644</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>91</td>
  <td><a href="/wiki/Ulhasnagar" title="Ulhasnagar">Ulhasnagar</a></td>
  <td>506,937</td>
  <td>473,731</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>92</td>
  <td><b><a href="/wiki/Jammu" title="Jammu">Jammu</a></b><sup class="reference" id="cite_ref-13"><a href="#cite_note-13">[12]</a></sup></td>
  <td>503,690</td>
  <td>369,959</td>
  <td><a href="/wiki/Jammu_and_Kashmir" title="Jammu and Kashmir">Jammu and Kashmir</a>
  </td></tr>
  <tr>
  <td>93</td>
  <td><a href="/wiki/Sangli-Miraj_%26_Kupwad" title="Sangli-Miraj &amp; Kupwad">Sangli-Miraj &amp; Kupwad</a></td>
  <td>502,697</td>
  <td>436,781</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>94</td>
  <td><a href="/wiki/Mangalore" title="Mangalore">Mangalore</a></td>
  <td>499,486</td>
  <td>399,565</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>95</td>
  <td><a href="/wiki/Erode" title="Erode">Erode</a><sup class="reference" id="cite_ref-14"><a href="#cite_note-14">[13]</a></sup></td>
  <td>498,129</td>
  <td>173,600</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>96</td>
  <td><a href="/wiki/Belgaum" title="Belgaum">Belgaum</a></td>
  <td>488,292</td>
  <td>399,653</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>97</td>
  <td><a href="/wiki/Ambattur" title="Ambattur">Ambattur</a></td>
  <td>478,134</td>
  <td>310,967</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>98</td>
  <td><a href="/wiki/Tirunelveli" title="Tirunelveli">Tirunelveli</a></td>
  <td>473,637</td>
  <td>411,831</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>99</td>
  <td><a href="/wiki/Malegaon" title="Malegaon">Malegaon</a></td>
  <td>471,006</td>
  <td>409,403</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr></tbody>], [<tbody><tr>
  <th width="5%">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-4"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>101</td>
  <td><a href="/wiki/Gaya,_India" title="Gaya, India">Gaya</a></td>
  <td>463,454</td>
  <td>385,432</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>102</td>
  <td><a href="/wiki/Jalgaon" title="Jalgaon">Jalgaon</a></td>
  <td>460,468</td>
  <td>368,618</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>103</td>
  <td><a href="/wiki/Udaipur" title="Udaipur">Udaipur</a></td>
  <td>451,735</td>
  <td>389,438</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr>
  <tr>
  <td>104</td>
  <td><a href="/wiki/Maheshtala" title="Maheshtala">Maheshtala</a></td>
  <td>449,423</td>
  <td>385,266</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>105</td>
  <td><a href="/wiki/Davanagere" title="Davanagere">Davanagere</a></td>
  <td>435,128</td>
  <td>364,523</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>106</td>
  <td><a href="/wiki/Kozhikode" title="Kozhikode">Kozhikode</a></td>
  <td>432,097</td>
  <td>436,556</td>
  <td><a href="/wiki/Kerala" title="Kerala">Kerala</a>
  </td></tr>
  <tr>
  <td>107</td>
  <td><a href="/wiki/Kurnool" title="Kurnool">Kurnool</a></td>
  <td>430,214</td>
  <td>269,122</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>108</td>
  <td><a href="/wiki/Rajpur_Sonarpur" title="Rajpur Sonarpur">Rajpur Sonarpur</a></td>
  <td>423,806</td>
  <td>336,707</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>109</td>
  <td><a href="/wiki/Rajahmundry" title="Rajahmundry">Rajahmundry</a><sup class="reference" id="cite_ref-15"><a href="#cite_note-15">[14]</a></sup><sup class="reference" id="cite_ref-16"><a href="#cite_note-16">[15]</a></sup></td>
  <td>419,818</td>
  <td>315,251</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>110</td>
  <td><a href="/wiki/Bokaro_Steel_City" title="Bokaro Steel City">Bokaro</a></td>
  <td>413,934</td>
  <td>393,805</td>
  <td><a href="/wiki/Jharkhand" title="Jharkhand">Jharkhand</a>
  </td></tr>
  <tr>
  <td>111</td>
  <td><a href="/wiki/South_Dumdum" title="South Dumdum">South Dumdum</a></td>
  <td>410,524</td>
  <td>392,444</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>112</td>
  <td><a href="/wiki/Bellary" title="Bellary">Bellary</a></td>
  <td>409,644</td>
  <td>316,766</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>113</td>
  <td><a href="/wiki/Patiala" title="Patiala">Patiala</a></td>
  <td>405,164</td>
  <td>303,151</td>
  <td><a class="mw-redirect" href="/wiki/Punjab_(India)" title="Punjab (India)">Punjab</a>
  </td></tr>
  <tr>
  <td>114</td>
  <td><a class="mw-redirect" href="/wiki/Gopalpur,_West_Bengal" title="Gopalpur, West Bengal">Gopalpur</a></td>
  <td>404,991</td>
  <td>271,811</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>115</td>
  <td><b><a href="/wiki/Agartala" title="Agartala">Agartala</a></b></td>
  <td>399,688</td>
  <td>271,811</td>
  <td><a href="/wiki/Tripura" title="Tripura">Tripura</a>
  </td></tr>
  <tr>
  <td>116</td>
  <td><a href="/wiki/Bhagalpur" title="Bhagalpur">Bhagalpur</a></td>
  <td>398,138</td>
  <td>340,767</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>117</td>
  <td><a href="/wiki/Muzaffarnagar" title="Muzaffarnagar">Muzaffarnagar</a></td>
  <td>392,451</td>
  <td>316,729</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>118</td>
  <td><a href="/wiki/Bhatpara" title="Bhatpara">Bhatpara</a></td>
  <td>390,467</td>
  <td>442,385</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>119</td>
  <td><a href="/wiki/Panihati" title="Panihati">Panihati</a></td>
  <td>383,522</td>
  <td>348,438</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>120</td>
  <td><a href="/wiki/Latur" title="Latur">Latur</a></td>
  <td>382,754</td>
  <td>299,985</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>121</td>
  <td><a href="/wiki/Dhule" title="Dhule">Dhule</a></td>
  <td>376,093</td>
  <td>341,755</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>122</td>
  <td><a href="/wiki/Tirupati" title="Tirupati">Tirupati</a><sup class="reference" id="cite_ref-17"><a href="#cite_note-17">[16]</a></sup></td>
  <td>374,260</td>
  <td>228,202</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>123</td>
  <td><a href="/wiki/Rohtak" title="Rohtak">Rohtak</a></td>
  <td>373,133</td>
  <td>286,807</td>
  <td><a href="/wiki/Haryana" title="Haryana">Haryana</a>
  </td></tr>
  <tr>
  <td>124</td>
  <td><a href="/wiki/Korba,_Chhattisgarh" title="Korba, Chhattisgarh">Korba</a></td>
  <td>363,210</td>
  <td>315,690</td>
  <td><a href="/wiki/Chhattisgarh" title="Chhattisgarh">Chhattisgarh</a>
  </td></tr>
  <tr>
  <td>125</td>
  <td><a href="/wiki/Bhilwara" title="Bhilwara">Bhilwara</a></td>
  <td>360,009</td>
  <td>280,128</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr></tbody>], [<tbody><tr>
  <th width="5%">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-5"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>126</td>
  <td><a href="/wiki/Berhampur" title="Berhampur">Berhampur</a></td>
  <td>355,823</td>
  <td>307,792</td>
  <td><a href="/wiki/Odisha" title="Odisha">Odisha</a>
  </td></tr>
  <tr>
  <td>127</td>
  <td><a href="/wiki/Muzaffarpur" title="Muzaffarpur">Muzaffarpur</a></td>
  <td>351,838</td>
  <td>305,525</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>128</td>
  <td><a href="/wiki/Ahmednagar" title="Ahmednagar">Ahmednagar</a></td>
  <td>350,905</td>
  <td>307,615</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>129</td>
  <td><a href="/wiki/Mathura" title="Mathura">Mathura</a></td>
  <td>349,336</td>
  <td>302,770</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>130</td>
  <td><a href="/wiki/Kollam" title="Kollam">Kollam</a></td>
  <td>349,033</td>
  <td>361,560</td>
  <td><a href="/wiki/Kerala" title="Kerala">Kerala</a>
  </td></tr>
  <tr>
  <td>131</td>
  <td><a href="/wiki/Avadi" title="Avadi">Avadi</a></td>
  <td>344,701</td>
  <td>229,403</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>132</td>
  <td><a href="/wiki/Kadapa" title="Kadapa">Kadapa</a></td>
  <td>343,054</td>
  <td>125,725</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>133</td>
  <td><a href="/wiki/Kamarhati" title="Kamarhati">Kamarhati</a></td>
  <td>336,579</td>
  <td>314,507</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>134</td>
  <td><a href="/wiki/Sambalpur" title="Sambalpur">Sambalpur</a></td>
  <td>335,761</td>
  <td>296,662</td>
  <td><a href="/wiki/Odisha" title="Odisha">Odisha</a>
  </td></tr>
  <tr>
  <td>135</td>
  <td><a href="/wiki/Bilaspur,_Chhattisgarh" title="Bilaspur, Chhattisgarh">Bilaspur</a></td>
  <td>330,106</td>
  <td>274,917</td>
  <td><a href="/wiki/Chhattisgarh" title="Chhattisgarh">Chhattisgarh</a>
  </td></tr>
  <tr>
  <td>136</td>
  <td><a href="/wiki/Shahjahanpur" title="Shahjahanpur">Shahjahanpur</a></td>
  <td>327,975</td>
  <td>296,662</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>137</td>
  <td><a href="/wiki/Satara_(city)" title="Satara (city)">Satara</a></td>
  <td>326,789</td>
  <td>228,175</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>138</td>
  <td><a class="mw-redirect" href="/wiki/Bijapur,_Karnataka" title="Bijapur, Karnataka">Bijapur</a></td>
  <td>326,360</td>
  <td>228,175</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>139</td>
  <td><a href="/wiki/Rampur,_Uttar_Pradesh" title="Rampur, Uttar Pradesh">Rampur</a></td>
  <td>325,248</td>
  <td>281,494</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>140</td>
  <td><a class="mw-redirect" href="/wiki/Shivamogga" title="Shivamogga">Shivamogga</a></td>
  <td>322,428</td>
  <td>274,352</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>141</td>
  <td><a href="/wiki/Chandrapur" title="Chandrapur">Chandrapur</a></td>
  <td>321,036</td>
  <td>289,450</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>142</td>
  <td><a href="/wiki/Junagadh" title="Junagadh">Junagadh</a></td>
  <td>320,250</td>
  <td>168,686</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>143</td>
  <td><a href="/wiki/Thrissur" title="Thrissur">Thrissur</a></td>
  <td>315,596</td>
  <td>317,526</td>
  <td><a href="/wiki/Kerala" title="Kerala">Kerala</a>
  </td></tr>
  <tr>
  <td>144</td>
  <td><a href="/wiki/Alwar" title="Alwar">Alwar</a></td>
  <td>315,310</td>
  <td>260,593</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr>
  <tr>
  <td>145</td>
  <td><a href="/wiki/Bardhaman" title="Bardhaman">Bardhaman</a></td>
  <td>314,638</td>
  <td>285,602</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>146</td>
  <td><a href="/wiki/Kulti" title="Kulti">Kulti</a></td>
  <td>313,977</td>
  <td>289,903</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>147</td>
  <td><a href="/wiki/Kakinada" title="Kakinada">Kakinada</a></td>
  <td>325,985</td>
  <td>296,329</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>148</td>
  <td><a href="/wiki/Nizamabad,_Telangana" title="Nizamabad, Telangana">Nizamabad</a></td>
  <td>310,467</td>
  <td>288,722</td>
  <td><a href="/wiki/Telangana" title="Telangana">Telangana</a>
  </td></tr>
  <tr>
  <td>149</td>
  <td><a href="/wiki/Parbhani" title="Parbhani">Parbhani</a></td>
  <td>307,191</td>
  <td>259,329</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>150</td>
  <td><a href="/wiki/Tumkur" title="Tumkur">Tumkur</a></td>
  <td>305,821</td>
  <td>248,929</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr></tbody>], [<tbody><tr>
  <th width="5%">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-6"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>151</td>
  <td><a href="/wiki/Khammam" title="Khammam">Khammam</a></td>
  <td>305,000</td>
  <td>218,689</td>
  <td><a href="/wiki/Telangana" title="Telangana">Telangana</a>
  </td></tr>
  <tr>
  <td>152</td>
  <td><a href="/wiki/Ozhukarai" title="Ozhukarai">Ozhukarai</a></td>
  <td>300,028</td>
  <td>217,707</td>
  <td><a href="/wiki/Puducherry" title="Puducherry">Puducherry</a>
  </td></tr>
  <tr>
  <td>153</td>
  <td><a href="/wiki/Bihar_Sharif" title="Bihar Sharif">Bihar Sharif</a></td>
  <td>296,889</td>
  <td>232,071</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>154</td>
  <td><a href="/wiki/Panipat" title="Panipat">Panipat</a></td>
  <td>294,150</td>
  <td>261,740</td>
  <td><a href="/wiki/Haryana" title="Haryana">Haryana</a>
  </td></tr>
  <tr>
  <td>155</td>
  <td><a href="/wiki/Darbhanga" title="Darbhanga">Darbhanga</a></td>
  <td>294,116</td>
  <td>267,348</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>156</td>
  <td><a href="/wiki/Bally,_Howrah" title="Bally, Howrah">Bally</a></td>
  <td>291,972</td>
  <td>260,906</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>157</td>
  <td><b><a href="/wiki/Aizawl" title="Aizawl">Aizawl</a></b></td>
  <td>291,822</td>
  <td>228,280</td>
  <td><a href="/wiki/Mizoram" title="Mizoram">Mizoram</a>
  </td></tr>
  <tr>
  <td>158</td>
  <td><a href="/wiki/Dewas" title="Dewas">Dewas</a></td>
  <td>289,438</td>
  <td>231,672</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>159</td>
  <td><a href="/wiki/Ichalkaranji" title="Ichalkaranji">Ichalkaranji</a></td>
  <td>287,570</td>
  <td>257,610</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>160</td>
  <td><a href="/wiki/Karnal" title="Karnal">Karnal</a></td>
  <td>286,974</td>
  <td>210,476</td>
  <td><a href="/wiki/Haryana" title="Haryana">Haryana</a>
  </td></tr>
  <tr>
  <td>161</td>
  <td><a href="/wiki/Bathinda" title="Bathinda">Bathinda</a></td>
  <td>285,813</td>
  <td>217,256</td>
  <td><a class="mw-redirect" href="/wiki/Punjab_(India)" title="Punjab (India)">Punjab</a>
  </td></tr>
  <tr>
  <td>162</td>
  <td><a class="mw-redirect" href="/wiki/Jalna_(city)" title="Jalna (city)">Jalna</a></td>
  <td>285,349</td>
  <td>235,795</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>163</td>
  <td><a href="/wiki/Eluru" title="Eluru">Eluru</a></td>
  <td>283,648<sup class="reference" id="cite_ref-18"><a href="#cite_note-18">[17]</a></sup></td>
  <td>190,347</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>164</td>
  <td><a href="/wiki/Kirari_Suleman_Nagar" title="Kirari Suleman Nagar">Kirari Suleman Nagar</a></td>
  <td>282,598</td>
  <td>153,874</td>
  <td><a href="/wiki/Delhi" title="Delhi">Delhi</a>
  </td></tr>
  <tr>
  <td>165</td>
  <td><a href="/wiki/Barasat" title="Barasat">Barasat</a></td>
  <td>283,443</td>
  <td>231,515</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>166</td>
  <td><a href="/wiki/Purnia" title="Purnia">Purnia</a></td>
  <td>280,547</td>
  <td>171,687<sup class="reference" id="cite_ref-19"><a href="#cite_note-19">[18]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>167</td>
  <td><a href="/wiki/Satna" title="Satna">Satna</a></td>
  <td>280,248</td>
  <td>225,464</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>168</td>
  <td><a href="/wiki/Mau" title="Mau">Mau</a></td>
  <td>279,060</td>
  <td>212,657</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>169</td>
  <td><a href="/wiki/Sonipat" title="Sonipat">Sonipat</a></td>
  <td>277,053</td>
  <td>214,974</td>
  <td><a href="/wiki/Haryana" title="Haryana">Haryana</a>
  </td></tr>
  <tr>
  <td>170</td>
  <td><a href="/wiki/Farrukhabad" title="Farrukhabad">Farrukhabad</a></td>
  <td>275,750</td>
  <td>228,333</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>171</td>
  <td><a href="/wiki/Sagar,_Madhya_Pradesh" title="Sagar, Madhya Pradesh">Sagar</a></td>
  <td>273,357</td>
  <td>232,133</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>172</td>
  <td><a href="/wiki/Rourkela" title="Rourkela">Rourkela</a></td>
  <td>273,217</td>
  <td>224,601</td>
  <td><a href="/wiki/Odisha" title="Odisha">Odisha</a>
  </td></tr>
  <tr>
  <td>173</td>
  <td><a href="/wiki/Durg" title="Durg">Durg</a></td>
  <td>268,679</td>
  <td>232,517</td>
  <td><a href="/wiki/Chhattisgarh" title="Chhattisgarh">Chhattisgarh</a>
  </td></tr>
  <tr>
  <td>174</td>
  <td><b><a href="/wiki/Imphal" title="Imphal">Imphal</a></b></td>
  <td>264,986</td>
  <td>221,492</td>
  <td><a href="/wiki/Manipur" title="Manipur">Manipur</a>
  </td></tr>
  <tr>
  <td>175</td>
  <td><a href="/wiki/Ratlam" title="Ratlam">Ratlam</a></td>
  <td>264,810</td>
  <td>222,202</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr></tbody>], [<tbody><tr>
  <th width="5%">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-7"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>176</td>
  <td><a href="/wiki/Hapur" title="Hapur">Hapur</a></td>
  <td>262,801</td>
  <td>211,983</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>177</td>
  <td><a href="/wiki/Arrah" title="Arrah">Arrah</a></td>
  <td>261,099</td>
  <td>203,380</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>178</td>
  <td><a href="/wiki/Karimnagar" title="Karimnagar">Karimnagar</a></td>
  <td>260,899</td>
  <td>205,653</td>
  <td><a href="/wiki/Telangana" title="Telangana">Telangana</a>
  </td></tr>
  <tr>
  <td>179</td>
  <td><a href="/wiki/Anantapur" title="Anantapur">Anantapur</a></td>
  <td>261,004</td>
  <td>218,808</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>180</td>
  <td><a href="/wiki/Etawah" title="Etawah">Etawah</a></td>
  <td>256,838</td>
  <td>210,453</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>181</td>
  <td><a class="mw-redirect" href="/wiki/Ambernath" title="Ambernath">Ambernath</a></td>
  <td>254,003</td>
  <td>203,795</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>182</td>
  <td><a href="/wiki/North_Dumdum" title="North Dumdum">North Dumdum</a></td>
  <td>253,625</td>
  <td>220,042</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>183</td>
  <td><a class="mw-redirect" href="/wiki/Bharatpur,_India" title="Bharatpur, India">Bharatpur</a></td>
  <td>252,109</td>
  <td>204,587</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr>
  <tr>
  <td>184</td>
  <td><a href="/wiki/Begusarai" title="Begusarai">Begusarai</a></td>
  <td>251,136</td>
  <td>93,378</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>185</td>
  <td><a href="/wiki/New_Delhi" title="New Delhi">New Delhi</a></td>
  <td>249,998</td>
  <td>302,147</td>
  <td><a href="/wiki/Delhi" title="Delhi">Delhi</a>
  </td></tr>
  <tr>
  <td>186</td>
  <td><a href="/wiki/Gandhidham" title="Gandhidham">Gandhidham</a></td>
  <td>248,705</td>
  <td>166,388</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>187</td>
  <td><a href="/wiki/Baranagar" title="Baranagar">Baranagar</a></td>
  <td>248,466</td>
  <td>250,768</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>188</td>
  <td><a href="/wiki/Tiruvottiyur" title="Tiruvottiyur">Tiruvottiyur</a></td>
  <td>248,059</td>
  <td>212,281</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>189</td>
  <td><b><a href="/wiki/Pondicherry" title="Pondicherry">Pondicherry</a></b></td>
  <td>241,773</td>
  <td>220,749</td>
  <td><a href="/wiki/Puducherry" title="Puducherry">Puducherry</a>
  </td></tr>
  <tr>
  <td>190</td>
  <td><a href="/wiki/Sikar" title="Sikar">Sikar</a></td>
  <td>237,579</td>
  <td>184,904</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr>
  <tr>
  <td>191</td>
  <td><a href="/wiki/Thoothukudi" title="Thoothukudi">Thoothukudi</a></td>
  <td>237,374</td>
  <td>216,058</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>192</td>
  <td><a class="mw-redirect" href="/wiki/Rewa,_India" title="Rewa, India">Rewa</a></td>
  <td>235,422</td>
  <td>183,274</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>193</td>
  <td><a href="/wiki/Mirzapur" title="Mirzapur">Mirzapur</a></td>
  <td>233,691</td>
  <td>205,053</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>194</td>
  <td><a href="/wiki/Raichur" title="Raichur">Raichur</a></td>
  <td>232,456</td>
  <td>207,421</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>195</td>
  <td><a href="/wiki/Pali,_Rajasthan" title="Pali, Rajasthan">Pali</a></td>
  <td>229,956</td>
  <td>187,641</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr>
  <tr>
  <td>196</td>
  <td><a href="/wiki/Ramagundam" title="Ramagundam">Ramagundam</a><sup class="reference" id="cite_ref-20"><a href="#cite_note-20">[19]</a></sup></td>
  <td>229,644</td>
  <td>236,600</td>
  <td><a href="/wiki/Telangana" title="Telangana">Telangana</a>
  </td></tr>
  <tr>
  <td>197</td>
  <td><a href="/wiki/Haridwar" title="Haridwar">Haridwar</a></td>
  <td>228,832</td>
  <td>175,010</td>
  <td><a href="/wiki/Uttarakhand" title="Uttarakhand">Uttarakhand</a>
  </td></tr>
  <tr>
  <td>198</td>
  <td><a href="/wiki/Vizianagaram" title="Vizianagaram">Vijayanagaram</a></td>
  <td>228,025</td>
  <td>174,324</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>199</td>
  <td><a href="/wiki/Katihar" title="Katihar">Katihar</a></td>
  <td>225,982</td>
  <td>175,169</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>200</td>
  <td><a href="/wiki/Nagercoil" title="Nagercoil">Nagercoil</a></td>
  <td>224,849</td>
  <td>208,179</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr></tbody>], [<tbody><tr>
  <th width="5%">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-8"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>201</td>
  <td><a href="/wiki/Sri_Ganganagar" title="Sri Ganganagar">Sri Ganganagar</a></td>
  <td>224,773</td>
  <td>210,713</td>
  <td><a href="/wiki/Rajasthan" title="Rajasthan">Rajasthan</a>
  </td></tr>
  <tr>
  <td>202</td>
  <td><a href="/wiki/Karawal_Nagar" title="Karawal Nagar">Karawal Nagar</a></td>
  <td>224,666</td>
  <td>148,549</td>
  <td><a href="/wiki/Delhi" title="Delhi">Delhi</a>
  </td></tr>
  <tr>
  <td>203</td>
  <td><a href="/wiki/Mango_(Jamshedpur)" title="Mango (Jamshedpur)">Mango</a></td>
  <td>223,805</td>
  <td>166,125</td>
  <td><a href="/wiki/Jharkhand" title="Jharkhand">Jharkhand</a>
  </td></tr>
  <tr>
  <td>204</td>
  <td><a href="/wiki/Thanjavur" title="Thanjavur">Thanjavur</a></td>
  <td>222,943</td>
  <td>215,314</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>205</td>
  <td><a href="/wiki/Bulandshahr" title="Bulandshahr">Bulandshahr</a></td>
  <td>222,519</td>
  <td>176,425</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>206</td>
  <td><a href="/wiki/Uluberia" title="Uluberia">Uluberia</a></td>
  <td>222,240</td>
  <td>202,135</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>207</td>
  <td><a class="mw-redirect" href="/wiki/Murwara" title="Murwara">Murwara</a></td>
  <td>221,883</td>
  <td>187,029
  </td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>208</td>
  <td><a href="/wiki/Sambhal" title="Sambhal">Sambhal</a></td>
  <td>220,813</td>
  <td>182,478
  </td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>209</td>
  <td><a href="/wiki/Singrauli" title="Singrauli">Singrauli</a></td>
  <td>220,257</td>
  <td>185,190</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>210</td>
  <td><a href="/wiki/Nadiad" title="Nadiad">Nadiad</a></td>
  <td>218,095</td>
  <td>192,913</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>211</td>
  <td><a href="/wiki/Secunderabad" title="Secunderabad">Secunderabad</a></td>
  <td>217,910</td>
  <td>206,102</td>
  <td><a href="/wiki/Telangana" title="Telangana">Telangana</a>
  </td></tr>
  <tr>
  <td>212</td>
  <td><a href="/wiki/Naihati" title="Naihati">Naihati</a></td>
  <td>217,900</td>
  <td>215,303</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>213</td>
  <td><a href="/wiki/Yamunanagar" title="Yamunanagar">Yamunanagar</a></td>
  <td>216,677</td>
  <td>189,696</td>
  <td><a href="/wiki/Haryana" title="Haryana">Haryana</a>
  </td></tr>
  <tr>
  <td>214</td>
  <td><a class="mw-redirect" href="/wiki/Bidhan_Nagar" title="Bidhan Nagar">Bidhan Nagar</a></td>
  <td>215,514</td>
  <td>164,221</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>215</td>
  <td><a href="/wiki/Pallavaram" title="Pallavaram">Pallavaram</a></td>
  <td>215,417</td>
  <td>144,623</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>216</td>
  <td><a href="/wiki/Bidar" title="Bidar">Bidar</a></td>
  <td>214,373</td>
  <td>172,877</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>217</td>
  <td><a href="/wiki/Munger" title="Munger">Munger</a></td>
  <td>213,303</td>
  <td>188,050</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>218</td>
  <td><a href="/wiki/Panchkula" title="Panchkula">Panchkula</a></td>
  <td>211,355</td>
  <td>140,925
  </td>
  <td><a href="/wiki/Haryana" title="Haryana">Haryana</a>
  </td></tr>
  <tr>
  <td>219</td>
  <td><a href="/wiki/Burhanpur" title="Burhanpur">Burhanpur</a></td>
  <td>210,886</td>
  <td>193,725</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>220</td>
  <td><a href="/wiki/Raurkela_Industrial_Township" title="Raurkela Industrial Township">Raurkela Industrial Township</a></td>
  <td>210,317</td>
  <td>206,693</td>
  <td><a href="/wiki/Odisha" title="Odisha">Odisha</a>
  </td></tr>
  <tr>
  <td>221</td>
  <td><a href="/wiki/Kharagpur" title="Kharagpur">Kharagpur</a></td>
  <td>207,604</td>
  <td>188,761</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>222</td>
  <td><a href="/wiki/Dindigul" title="Dindigul">Dindigul</a></td>
  <td>207,327</td>
  <td>196,955</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>223</td>
  <td><b><a href="/wiki/Gandhinagar" title="Gandhinagar">Gandhinagar</a></b></td>
  <td>206,167</td>
  <td>195,985</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>224</td>
  <td><a href="/wiki/Hospet" title="Hospet">Hospet</a></td>
  <td>206,167</td>
  <td>164,240</td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>225</td>
  <td><a href="/wiki/Nangloi_Jat" title="Nangloi Jat">Nangloi Jat</a></td>
  <td>205,596</td>
  <td>150,948</td>
  <td><a href="/wiki/Delhi" title="Delhi">Delhi</a>
  </td></tr></tbody>], [<tbody><tr>
  <th width="5%">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-9"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>226</td>
  <td><a class="mw-redirect" href="/wiki/English_Bazar" title="English Bazar">English Bazar</a></td>
  <td>205,521</td>
  <td>161,456</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>227</td>
  <td><a href="/wiki/Ongole" title="Ongole">Ongole</a></td>
  <td>204,746</td>
  <td>150,471</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>228</td>
  <td><a href="/wiki/Deoghar" title="Deoghar">Deoghar</a></td>
  <td>203,123</td>
  <td>112,525
  </td>
  <td><a href="/wiki/Jharkhand" title="Jharkhand">Jharkhand</a>
  </td></tr>
  <tr>
  <td>229</td>
  <td><a href="/wiki/Chhapra" title="Chhapra">Chapra</a></td>
  <td>202,352</td>
  <td>79,190</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>230</td>
  <td><a href="/wiki/Haldia" title="Haldia">Haldia</a></td>
  <td>200,827</td>
  <td>170,673</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>231</td>
  <td><a href="/wiki/Khandwa" title="Khandwa">Khandwa</a></td>
  <td>200,738</td>
  <td>172,242</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>232</td>
  <td><a href="/wiki/Nandyal" title="Nandyal">Nandyal</a></td>
  <td>200,516</td>
  <td>152,676</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>233</td>
  <td><a href="/wiki/Chittoor,_Andhra_Pradesh" title="Chittoor, Andhra Pradesh">Chittoor</a><sup class="reference" id="cite_ref-21"><a href="#cite_note-21">[20]</a></sup></td>
  <td>189,332</td>
  <td>152,654</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>234</td>
  <td><a href="/wiki/Morena" title="Morena">Morena</a></td>
  <td>200,482</td>
  <td>150,959</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>235</td>
  <td><a href="/wiki/Amroha" title="Amroha">Amroha</a></td>
  <td>198,471</td>
  <td>165,129</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>236</td>
  <td><a href="/wiki/Anand,_Gujarat" title="Anand, Gujarat">Anand</a></td>
  <td>198,282</td>
  <td>130,685</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>237</td>
  <td><a href="/wiki/Bhind" title="Bhind">Bhind</a></td>
  <td>197,585</td>
  <td>153,752</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>238</td>
  <td><a href="/wiki/Bhalswa_Jahangir_Pur" title="Bhalswa Jahangir Pur">Bhalswa Jahangir Pur</a></td>
  <td>197,148</td>
  <td>152,339</td>
  <td><a href="/wiki/Delhi" title="Delhi">Delhi</a>
  </td></tr>
  <tr>
  <td>239</td>
  <td><a href="/wiki/Madhyamgram" title="Madhyamgram">Madhyamgram</a></td>
  <td>196,127</td>
  <td>155,451</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>240</td>
  <td><a href="/wiki/Bhiwani" title="Bhiwani">Bhiwani</a></td>
  <td>196,057</td>
  <td>169,531</td>
  <td><a href="/wiki/Haryana" title="Haryana">Haryana</a>
  </td></tr>
  <tr>
  <td>241</td>
  <td><a href="/wiki/Navi_Mumbai" title="Navi Mumbai">Navi Mumbai</a> Panvel Raigad</td>
  <td>195,373</td>
  <td></td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>242</td>
  <td><a class="mw-redirect" href="/wiki/Baharampur" title="Baharampur">Baharampur</a></td>
  <td>195,223</td>
  <td>160,143</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>243</td>
  <td><a href="/wiki/Ambala" title="Ambala">Ambala</a></td>
  <td>195,153</td>
  <td>139,279</td>
  <td><a href="/wiki/Haryana" title="Haryana">Haryana</a>
  </td></tr>
  <tr>
  <td>244</td>
  <td><a href="/wiki/Morbi" title="Morbi">Morbi</a></td>
  <td>194,947</td>
  <td>145,719</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>245</td>
  <td><a href="/wiki/Fatehpur,_Uttar_Pradesh" title="Fatehpur, Uttar Pradesh">Fatehpur</a></td>
  <td>193,193</td>
  <td>151,757</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>246</td>
  <td><a class="mw-redirect" href="/wiki/Rae_Bareli" title="Rae Bareli">Rae Bareli</a></td>
  <td>191,316</td>
  <td>169,333</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>247</td>
  <td><a href="/wiki/Khora" title="Khora">Mahaboobnagar</a></td>
  <td>190,400</td>
  <td></td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Telangana</a>
  </td></tr>
  <tr>
  <td>248</td>
  <td><a href="/wiki/Bhusawal" title="Bhusawal">Bhusawal</a></td>
  <td>187,421</td>
  <td>172,372</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>249</td>
  <td><a href="/wiki/Orai" title="Orai">Orai</a></td>
  <td>187,137</td>
  <td>139,318</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>250</td>
  <td><a href="/wiki/Bahraich" title="Bahraich">Bahraich</a></td>
  <td>186,223</td>
  <td>168,323</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr></tbody>], [<tbody><tr>
  <th width="5%">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-10"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>251</td>
  <td><a href="/wiki/Vellore" title="Vellore">Vellore</a></td>
  <td>185,803</td>
  <td>177,230</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>252</td>
  <td><a class="mw-redirect" href="/wiki/Mahesana" title="Mahesana">Mahesana</a></td>
  <td>184,991</td>
  <td>141,453</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>253</td>
  <td><a href="/wiki/Sambalpur" title="Sambalpur">Sambalpur</a></td>
  <td>184,000</td>
  <td>153,643</td>
  <td><a class="mw-redirect" href="/wiki/Orissa,_India" title="Orissa, India">Orissa</a>
  </td></tr>
  <tr>
  <td>254</td>
  <td><a href="/wiki/Raiganj" title="Raiganj">Raiganj</a></td>
  <td>183,612</td>
  <td>165,212</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>255</td>
  <td><a href="/wiki/Sirsa" title="Sirsa">Sirsa</a></td>
  <td>182,534</td>
  <td>160,735</td>
  <td><a href="/wiki/Haryana" title="Haryana">Haryana</a>
  </td></tr>
  <tr>
  <td>256</td>
  <td><a href="/wiki/Danapur" title="Danapur">Danapur</a></td>
  <td>182,429</td>
  <td>131,176</td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>257</td>
  <td><a href="/wiki/Serampore" title="Serampore">Serampore</a></td>
  <td>181,842</td>
  <td>197,857</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>258</td>
  <td><a href="/wiki/Sultan_Pur_Majra" title="Sultan Pur Majra">Sultan Pur Majra</a></td>
  <td>181,554</td>
  <td>164,426</td>
  <td><a href="/wiki/Delhi" title="Delhi">Delhi</a>
  </td></tr>
  <tr>
  <td>259</td>
  <td><a href="/wiki/Guna,_India" title="Guna, India">Guna</a></td>
  <td>180,935</td>
  <td>137,175</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>260</td>
  <td><a href="/wiki/Jaunpur,_Uttar_Pradesh" title="Jaunpur, Uttar Pradesh">Jaunpur</a></td>
  <td>180,362</td>
  <td>160,055</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>261</td>
  <td><a href="/wiki/Panvel" title="Panvel">Panvel</a></td>
  <td>180,020</td>
  <td>104,058</td>
  <td><a href="/wiki/Maharashtra" title="Maharashtra">Maharashtra</a>
  </td></tr>
  <tr>
  <td>262</td>
  <td><a href="/wiki/Shivpuri" title="Shivpuri">Shivpuri</a></td>
  <td>179,977</td>
  <td>146,892</td>
  <td><a href="/wiki/Madhya_Pradesh" title="Madhya Pradesh">Madhya Pradesh</a>
  </td></tr>
  <tr>
  <td>263</td>
  <td><a href="/wiki/Surendranagar_Dudhrej" title="Surendranagar Dudhrej">Surendranagar Dudhrej</a></td>
  <td>177,851</td>
  <td>156,161</td>
  <td><a href="/wiki/Gujarat" title="Gujarat">Gujarat</a>
  </td></tr>
  <tr>
  <td>264</td>
  <td><a href="/wiki/Unnao" title="Unnao">Unnao</a></td>
  <td>177,658</td>
  <td>144,662</td>
  <td><a href="/wiki/Uttar_Pradesh" title="Uttar Pradesh">Uttar Pradesh</a>
  </td></tr>
  <tr>
  <td>265</td>
  <td><a class="mw-redirect" href="/wiki/Hugli-Chinsura" title="Hugli-Chinsura">Hugli</a> and <a href="/wiki/Chinsurah" title="Chinsurah">Chinsurah</a></td>
  <td>177,259</td>
  <td>170,201</td>
  <td><a href="/wiki/West_Bengal" title="West Bengal">West Bengal</a>
  </td></tr>
  <tr>
  <td>266</td>
  <td><a href="/wiki/Alappuzha" title="Alappuzha">Alappuzha</a></td>
  <td>174,164</td>
  <td>177,029</td>
  <td><a href="/wiki/Kerala" title="Kerala">Kerala</a>
  </td></tr>
  <tr>
  <td>267</td>
  <td><a href="/wiki/Kottayam" title="Kottayam">Kottayam</a></td>
  <td>172,878</td>
  <td>129,894</td>
  <td><a href="/wiki/Kerala" title="Kerala">Kerala</a>
  </td></tr>
  <tr>
  <td>268</td>
  <td><a href="/wiki/Machilipatnam" title="Machilipatnam">Machilipatnam</a></td>
  <td>169,892</td>
  <td>179,353</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>269</td>
  <td><b><a href="/wiki/Shimla" title="Shimla">Shimla</a></b></td>
  <td>169,578</td>
  <td>142,555</td>
  <td><a href="/wiki/Himachal_Pradesh" title="Himachal Pradesh">Himachal Pradesh</a>
  </td></tr>
  <tr>
  <td>270</td>
  <td><a href="/wiki/Adoni" title="Adoni">Adoni</a></td>
  <td>166,537</td>
  <td></td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>271</td>
  <td><a href="/wiki/Udupi" title="Udupi">Udupi</a></td>
  <td>165,401</td>
  <td></td>
  <td><a href="/wiki/Karnataka" title="Karnataka">Karnataka</a>
  </td></tr>
  <tr>
  <td>272</td>
  <td><a href="/wiki/Tenali" title="Tenali">Tenali</a></td>
  <td>164,937</td>
  <td></td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>273</td>
  <td><a href="/wiki/Proddatur" title="Proddatur">Proddatur</a></td>
  <td>163,600</td>
  <td>86,896
  </td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>274</td>
  <td><a href="/wiki/Saharsa" title="Saharsa">Saharsa</a></td>
  <td>155,175</td>
  <td>125,167<sup class="reference" id="cite_ref-22"><a href="#cite_note-22">[21]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>275</td>
  <td><a href="/wiki/Hindupur" title="Hindupur">Hindupur</a></td>
  <td>151,835</td>
  <td></td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr></tbody>], [<tbody><tr>
  <th width="5%">Rank
  </th>
  <th style="width:15%;">City
  </th>
  <th style="width:25%;">Population<br/>(2011)<sup class="reference" id="cite_ref-Cities1Lakhandabove_3-11"><a href="#cite_note-Cities1Lakhandabove-3">[3]</a></sup>
  </th>
  <th style="width:25%;">Population<br/>(2001)
  </th>
  <th style="width:30%;">State or union territory
  </th></tr>
  <tr>
  <td>276
  </td>
  <td><a href="/wiki/Sasaram" title="Sasaram">Sasaram</a>
  </td>
  <td>147,396
  </td>
  <td>131,172<sup class="reference" id="cite_ref-Rohtas_23-0"><a href="#cite_note-Rohtas-23">[22]</a></sup>
  </td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>277</td>
  <td><a href="/wiki/Hajipur" title="Hajipur">Hajipur</a></td>
  <td>147,126</td>
  <td>119,412<sup class="reference" id="cite_ref-24"><a href="#cite_note-24">[23]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>278</td>
  <td><a href="/wiki/Bhimavaram" title="Bhimavaram">Bhimavaram</a></td>
  <td>142,280</td>
  <td>―</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>279
  </td>
  <td><a href="/wiki/Kumbakonam" title="Kumbakonam">Kumbakonam</a>
  </td>
  <td>140,056
  </td>
  <td>144,021
  </td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>280</td>
  <td><a href="/wiki/Dehri" title="Dehri">Dehri</a></td>
  <td>137,068</td>
  <td>119,057<sup class="reference" id="cite_ref-Rohtas_23-1"><a href="#cite_note-Rohtas-23">[22]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>281</td>
  <td><a href="/wiki/Madanapalle" title="Madanapalle">Madanapalle</a></td>
  <td>135,669</td>
  <td>―</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>282</td>
  <td><a href="/wiki/Siwan,_Bihar" title="Siwan, Bihar">Siwan</a></td>
  <td>134,458</td>
  <td>109,919<sup class="reference" id="cite_ref-25"><a href="#cite_note-25">[24]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>282</td>
  <td><a href="/wiki/Bettiah" title="Bettiah">Bettiah</a></td>
  <td>132,896</td>
  <td>116,670<sup class="reference" id="cite_ref-PaschimChamparan_26-0"><a href="#cite_note-PaschimChamparan-26">[25]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>283</td>
  <td><a href="/wiki/Guntakal" title="Guntakal">Guntakal</a></td>
  <td>126,270</td>
  <td>―</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>284</td>
  <td><a href="/wiki/Srikakulam" title="Srikakulam">Srikakulam</a></td>
  <td>125,939</td>
  <td>―</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>285</td>
  <td><a href="/wiki/Motihari" title="Motihari">Motihari</a></td>
  <td>125,183</td>
  <td>100,683<sup class="reference" id="cite_ref-27"><a href="#cite_note-27">[26]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>286</td>
  <td><a href="/wiki/Dharmavaram,_Anantapur_district" title="Dharmavaram, Anantapur district">Dharmavaram</a></td>
  <td>121,874</td>
  <td>―</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>287</td>
  <td><a href="/wiki/Gudivada" title="Gudivada">Gudivada</a></td>
  <td>118,167</td>
  <td>―</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>288</td>
  <td><a href="/wiki/Phagwara" title="Phagwara">Phagwara</a></td>
  <td>117,966</td>
  <td>―</td>
  <td><a href="/wiki/Punjab" title="Punjab">Punjab</a>
  </td></tr>
  <tr>
  <td>288</td>
  <td><a href="/wiki/Narasaraopet" title="Narasaraopet">Narasaraopet</a></td>
  <td>116,250</td>
  <td>―</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>289</td>
  <td><a href="/wiki/Suryapet" title="Suryapet">Suryapet</a></td>
  <td>115,250</td>
  <td>94,585</td>
  <td><a href="/wiki/Telangana" title="Telangana">Telangana</a>
  </td></tr>
  <tr>
  <td>290</td>
  <td><a href="/wiki/Tadipatri" title="Tadipatri">Tadipatri</a></td>
  <td>108,171</td>
  <td>―</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>291</td>
  <td><a href="/wiki/Kishanganj" title="Kishanganj">Kishanganj</a></td>
  <td>107,076</td>
  <td>85,590<sup class="reference" id="cite_ref-28"><a href="#cite_note-28">[27]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>292</td>
  <td><a href="/wiki/Karaikudi" title="Karaikudi">Karaikudi</a></td>
  <td>106,714</td>
  <td>86,596</td>
  <td><a href="/wiki/Tamil_Nadu" title="Tamil Nadu">Tamil Nadu</a>
  </td></tr>
  <tr>
  <td>293</td>
  <td><a href="/wiki/Miryalaguda" title="Miryalaguda">Miryalaguda</a></td>
  <td>109,891</td>
  <td>91,395</td>
  <td><a href="/wiki/Telangana" title="Telangana">Telangana</a>
  </td></tr>
  <tr>
  <td>294</td>
  <td><a href="/wiki/Jamalpur,_Bihar" title="Jamalpur, Bihar">Jamalpur</a></td>
  <td>105,221</td>
  <td>96,983<sup class="reference" id="cite_ref-29"><a href="#cite_note-29">[28]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>295</td>
  <td><a href="/wiki/Kavali" title="Kavali">Kavali</a></td>
  <td>104,000</td>
  <td>―</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>296</td>
  <td><a href="/wiki/Tadepalligudem" title="Tadepalligudem">Tadepalligudem</a></td>
  <td>103,906</td>
  <td>―</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>297</td>
  <td><b><a href="/wiki/Amaravati" title="Amaravati">Amaravati</a></b></td>
  <td>103,000</td>
  <td>―</td>
  <td><a href="/wiki/Andhra_Pradesh" title="Andhra Pradesh">Andhra Pradesh</a>
  </td></tr>
  <tr>
  <td>298</td>
  <td><a href="/wiki/Buxar" title="Buxar">Buxar</a></td>
  <td>102,591</td>
  <td>83,168<sup class="reference" id="cite_ref-30"><a href="#cite_note-30">[29]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>299</td>
  <td><a href="/wiki/Jehanabad" title="Jehanabad">Jehanabad</a></td>
  <td>102,456</td>
  <td>81,503<sup class="reference" id="cite_ref-31"><a href="#cite_note-31">[30]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>300</td>
  <td><a href="/wiki/Aurangabad,_Bihar" title="Aurangabad, Bihar">Aurangabad</a></td>
  <td>101,520</td>
  <td>79,393<sup class="reference" id="cite_ref-32"><a href="#cite_note-32">[31]</a></sup></td>
  <td><a href="/wiki/Bihar" title="Bihar">Bihar</a>
  </td></tr>
  <tr>
  <td>301</td>
  <td><b><a href="/wiki/Gangtok" title="Gangtok">Gangtok</a></b></td>
  <td>100,286</td>
  <td>29,354</td>
  <td><a href="/wiki/Sikkim" title="Sikkim">Sikkim</a>
  </td></tr></tbody>]]
In [11]:
tr = []
for trow in tb:
    tr.append(trow[0].findAll('tr'))
In [12]:
cities = []

for t_r in tr:
    for i in range(1,len(t_r)):
        cities.append(t_r[i].find('a').text)
In [13]:
tr[1][13].find('a').text
Out[13]:
'Ranchi'
In [14]:
len(cities)
Out[14]:
302
In [15]:
cities
Out[15]:
['Mumbai',
 'Delhi',
 'Bangalore',
 'Hyderabad',
 'Ahmedabad',
 'Chennai',
 'Kolkata',
 'Surat',
 'Pune',
 'Jaipur',
 'Lucknow',
 'Kanpur',
 'Nagpur',
 'Indore',
 'Thane',
 'Bhopal',
 'Visakhapatnam',
 'Pimpri-Chinchwad',
 'Patna',
 'Vadodara',
 'Ghaziabad',
 'Ludhiana',
 'Agra',
 'Nashik',
 'Faridabad',
 'Meerut',
 'Rajkot',
 'Kalyan-Dombivali',
 'Vasai-Virar',
 'Varanasi',
 'Srinagar',
 'Aurangabad',
 'Dhanbad',
 'Amritsar',
 'Navi Mumbai',
 'Allahabad',
 'Howrah',
 'Ranchi',
 'Gwalior',
 'Jabalpur',
 'Coimbatore',
 'Vijayawada',
 'Jodhpur',
 'Madurai',
 'Raipur',
 'Kota',
 'Chandigarh',
 'Guwahati',
 'Solapur',
 'Hubballi-Dharwad',
 'Tiruchirappalli',
 'Bareilly',
 'Mysore',
 'Tiruppur',
 'Gurgaon',
 'Aligarh',
 'Jalandhar',
 'Bhubaneswar',
 'Salem',
 'Mira-Bhayandar',
 'Warangal',
 'Thiruvananthapuram',
 'Guntur',
 'Bhiwandi',
 'Saharanpur',
 'Gorakhpur',
 'Bikaner',
 'Amravati',
 'Noida',
 'Jamshedpur',
 'Bhilai',
 'Cuttack',
 'Firozabad',
 'Kochi',
 'Nellore',
 'Bhavnagar',
 'Dehradun',
 'Durgapur',
 'Asansol',
 'Rourkela',
 'Nanded',
 'Kolhapur',
 'Ajmer',
 'Akola',
 'Gulbarga',
 'Jamnagar',
 'Ujjain',
 'Loni',
 'Siliguri',
 'Jhansi',
 'Ulhasnagar',
 'Jammu',
 'Sangli-Miraj & Kupwad',
 'Mangalore',
 'Erode',
 'Belgaum',
 'Ambattur',
 'Tirunelveli',
 'Malegaon',
 'Gaya',
 'Jalgaon',
 'Udaipur',
 'Maheshtala',
 'Davanagere',
 'Kozhikode',
 'Kurnool',
 'Rajpur Sonarpur',
 'Rajahmundry',
 'Bokaro',
 'South Dumdum',
 'Bellary',
 'Patiala',
 'Gopalpur',
 'Agartala',
 'Bhagalpur',
 'Muzaffarnagar',
 'Bhatpara',
 'Panihati',
 'Latur',
 'Dhule',
 'Tirupati',
 'Rohtak',
 'Korba',
 'Bhilwara',
 'Berhampur',
 'Muzaffarpur',
 'Ahmednagar',
 'Mathura',
 'Kollam',
 'Avadi',
 'Kadapa',
 'Kamarhati',
 'Sambalpur',
 'Bilaspur',
 'Shahjahanpur',
 'Satara',
 'Bijapur',
 'Rampur',
 'Shivamogga',
 'Chandrapur',
 'Junagadh',
 'Thrissur',
 'Alwar',
 'Bardhaman',
 'Kulti',
 'Kakinada',
 'Nizamabad',
 'Parbhani',
 'Tumkur',
 'Khammam',
 'Ozhukarai',
 'Bihar Sharif',
 'Panipat',
 'Darbhanga',
 'Bally',
 'Aizawl',
 'Dewas',
 'Ichalkaranji',
 'Karnal',
 'Bathinda',
 'Jalna',
 'Eluru',
 'Kirari Suleman Nagar',
 'Barasat',
 'Purnia',
 'Satna',
 'Mau',
 'Sonipat',
 'Farrukhabad',
 'Sagar',
 'Rourkela',
 'Durg',
 'Imphal',
 'Ratlam',
 'Hapur',
 'Arrah',
 'Karimnagar',
 'Anantapur',
 'Etawah',
 'Ambernath',
 'North Dumdum',
 'Bharatpur',
 'Begusarai',
 'New Delhi',
 'Gandhidham',
 'Baranagar',
 'Tiruvottiyur',
 'Pondicherry',
 'Sikar',
 'Thoothukudi',
 'Rewa',
 'Mirzapur',
 'Raichur',
 'Pali',
 'Ramagundam',
 'Haridwar',
 'Vijayanagaram',
 'Katihar',
 'Nagercoil',
 'Sri Ganganagar',
 'Karawal Nagar',
 'Mango',
 'Thanjavur',
 'Bulandshahr',
 'Uluberia',
 'Murwara',
 'Sambhal',
 'Singrauli',
 'Nadiad',
 'Secunderabad',
 'Naihati',
 'Yamunanagar',
 'Bidhan Nagar',
 'Pallavaram',
 'Bidar',
 'Munger',
 'Panchkula',
 'Burhanpur',
 'Raurkela Industrial Township',
 'Kharagpur',
 'Dindigul',
 'Gandhinagar',
 'Hospet',
 'Nangloi Jat',
 'English Bazar',
 'Ongole',
 'Deoghar',
 'Chapra',
 'Haldia',
 'Khandwa',
 'Nandyal',
 'Chittoor',
 'Morena',
 'Amroha',
 'Anand',
 'Bhind',
 'Bhalswa Jahangir Pur',
 'Madhyamgram',
 'Bhiwani',
 'Navi Mumbai',
 'Baharampur',
 'Ambala',
 'Morbi',
 'Fatehpur',
 'Rae Bareli',
 'Mahaboobnagar',
 'Bhusawal',
 'Orai',
 'Bahraich',
 'Vellore',
 'Mahesana',
 'Sambalpur',
 'Raiganj',
 'Sirsa',
 'Danapur',
 'Serampore',
 'Sultan Pur Majra',
 'Guna',
 'Jaunpur',
 'Panvel',
 'Shivpuri',
 'Surendranagar Dudhrej',
 'Unnao',
 'Hugli',
 'Alappuzha',
 'Kottayam',
 'Machilipatnam',
 'Shimla',
 'Adoni',
 'Udupi',
 'Tenali',
 'Proddatur',
 'Saharsa',
 'Hindupur',
 'Sasaram',
 'Hajipur',
 'Bhimavaram',
 'Kumbakonam',
 'Dehri',
 'Madanapalle',
 'Siwan',
 'Bettiah',
 'Guntakal',
 'Srikakulam',
 'Motihari',
 'Dharmavaram',
 'Gudivada',
 'Phagwara',
 'Narasaraopet',
 'Suryapet',
 'Tadipatri',
 'Kishanganj',
 'Karaikudi',
 'Miryalaguda',
 'Jamalpur',
 'Kavali',
 'Tadepalligudem',
 'Amaravati',
 'Buxar',
 'Jehanabad',
 'Aurangabad',
 'Gangtok']
In [ ]:
 
