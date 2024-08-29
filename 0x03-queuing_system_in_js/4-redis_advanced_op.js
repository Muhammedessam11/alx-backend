import { createClient, print } from 'redis';

const client = createClient();

client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
client.on('connect', () => console.log('Redis client connected to the server'));

const hashObj = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2,
};

function setNewSchool(schoolName, field, value) {
  client.hset(schoolName, field, value, print);
}

async function displaySchoolValue(schoolName) {
  await client.hgetall(schoolName, (_err, rep) => {
    console.log(rep);
  });
}

for (const [field, value] of Object.entries(hashObj)) {
  setNewSchool('HolbertonSchools', field, value);
}

displaySchoolValue('HolbertonSchools');
